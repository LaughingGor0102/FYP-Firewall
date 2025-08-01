# FYP-Firewall
My fyp was making a firewall solution by using Python.

# Firewall Code - README

This README file provides step-by-step instructions on how to set up, run, and use the provided Python-based firewall code in **Visual Studio Code (VS Code)** or the **Command Prompt** on a Windows system.

-----------------------------------------------------------------------------------------------------------------------------------

## Prerequisites

Before running the firewall code, ensure the following prerequisites are met:

1. **Python Installation**:
   - Download and install Python (version 3.7 or later) from the [official Python website](https://www.python.org/).
   - During installation, make sure to check the box **"Add Python to PATH"**.

2. **Required Python Libraries**:
   - The code may require additional Python libraries. If any libraries are missing, you can install them using `pip` (Python's package manager). Instructions are provided below.

3. **Code Files**:
   - Ensure you have the Python script file(s) for the firewall code in a specific folder on your computer.

-----------------------------------------------------------------------------------------------------------------------------------

## Running the Firewall Code in VS Code

### Step 1: Install VS Code
- Download and install **Visual Studio Code** from the [official website](https://code.visualstudio.com/).

### Step 2: Install Python Extension for VS Code
- Open VS Code.
- Go to the **Extensions** view by clicking on the Extensions icon in the Activity Bar on the side of the window.
- Search for **"Python"** and install the official Python extension by Microsoft.

### Step 3: Open the Firewall Code in VS Code
- Open the folder containing the firewall Python script in VS Code:
  - Go to **File > Open Folder** and select the folder.
- Open the Python script file by clicking on it in the Explorer view.

### Step 4: Select Python Interpreter
- Press `Ctrl+Shift+P` to open the Command Palette.
- Type **"Python: Select Interpreter"** and select the Python latest version installed on your system.

### Step 5: Install Required Libraries
- Run the following command to install any required libraries:
  
  "pip install -r requirements.txt"
  
  If the `requirements.txt` file is not provided, manually install libraries using:
  
  "pip install <library_name>"
  
  Replace `<library_name>` with the name of the library (e.g., `socket`, `psutil`, etc.). Make sure all libraries and dependencies installed before running the firewall.

### Step 6: Run the Firewall Code
- Run the script by selecting **Run Python File** or **Run GUI File** from the menu.
- Alternatively, you can run the script in the terminal by typing:
  
  "python main.py"

         O R
  
  "python gui.py"

-----------------------------------------------------------------------------------------------------------------------------------

## Running the Firewall Code in Command Prompt

### Step 1: Open Command Prompt
- Press `Win + R`, type `cmd`, and press Enter to open the Command Prompt.

### Step 2: Navigate to the Script Directory
- Use the `cd` command to navigate to the folder containing the firewall Python script. For example:
  
  "cd C:\path\to\your\script". For example, "cd C:\Windows\User\file\firewall...".
  

### Step 3: Install Required Libraries
- Run the following command to install any required libraries:
  
  "pip install -r requirements.txt"
  
  If the `requirements.txt` file is not provided, manually install libraries using:
  
  "pip install <library_name>". For example, "pip install scapy". Make sure all libraries and dependencies installed before running the firewall.
  

### Step 4: Run the Firewall Code
- Run the script by typing after directory (cd) to the file location:
  
  "python main.py"

         O R
  
  "python gui.py"
  
-----------------------------------------------------------------------------------------------------------------------------------

## Features of the Firewall Code

The firewall code includes the following features:
- **Packet Filtering**: Inspects and filter network packets based on predefined rules. Blocks or allows network packets based on predefined rules.
- **IP & Port Blocking**: Restricts access and blocks traffic to specific IPs and Ports. 
- **IP Whitelisting/Blacklisting**: Allows or denies traffic from specific IP addresses.
- **ICMP Blocking**: Prevents ping floods or reconnaissance attempts.
- **Port Scanning Detection**: Detects and blocks IPs performing port scans.
- **Rate Limiting**: Blocks IPs sending packets at a high rate (e.g. Denial-of-Service (DoS) attack).
- **Logging**: Logs all network activities for monitoring purposes (allowed and blocked packets).
- **Custom Rules**: Users can define custom rules in the <config.json> for traffic filtering.

Refer to the comments in the Python code for more details on its functionality and how to customize it.

-----------------------------------------------------------------------------------------------------------------------------------

## Troubleshooting

1. **Python Not Recognized**:
   - Ensure Python is installed and added to the system PATH.
   - Verify by running `python --version` in Command Prompt.

2. **Missing Libraries**:
   - Install missing libraries using `pip install <library_name>`.

3. **Permission Issues**:
   - Run the Command Prompt or VS Code as an administrator since the script requires elevated privileges.

4. **Firewall Rules Not Working**:
   - Ensure the script is running with the necessary permissions to modify firewall settings.

-----------------------------------------------------------------------------------------------------------------------------------

## Notes

- Elevated/Root privileges required to run the code.
- Always test the firewall code in a safe environment before deploying it in a production system.
- Modify the script as needed to suit your specific requirements.
- Use caution when applying firewall rules to avoid accidentally blocking critical network traffic.

-----------------------------------------------------------------------------------------------------------------------------------

## Support

If you encounter any issues or have questions about the firewall code, feel free to reach out to the code's author or consult online Python documentation and forums.

