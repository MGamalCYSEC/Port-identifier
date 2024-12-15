# Port Identification Script

This script identifies the services associated with a list of ports provided by the user. It can read a list of ports from a file or directly from the command line. The script uses an extended database of known ports and their corresponding services, including commercial and non-commercial use cases.

## Features
- Identifies services associated with ports.
- Supports input from a file or directly from the command line.
- Includes a wide range of common ports used by applications, databases, protocols, and remote access services.
- Displays the service name for each port or marks it as "unknown" if it's not recognized.

## Prepration from scan

1. **Run Nmap Scan and Save to a File**:
   ```bash
   nmap -p- <target-ip> -oN nmap_scan.txt
   ```

2. Extract Ports with grep and awk
Now, you can extract just the port numbers from the Nmap scan result. Assuming you want to save each port on a new line, you can use the following command:
   ```bash
   grep -oP '\d+/tcp' nmap_scan.txt | awk -F/ '{print $1}' > ports.txt
   ```

3. **Run the script** directly:
   ```bash
   python port_identification_script.py
   ```

## Usage

### Option 1: Using a File
You can provide a text file that contains a list of ports (one port per line). The script will read the file and output the corresponding services for each port.

**Command**:
```bash
python port_identification_script.py -f ports.txt
```

### Option 2: Using Command-Line Ports
Alternatively, you can provide the ports directly from the command line using the `-p` option. Provide multiple ports separated by spaces.

**Command**:
```bash
python port_identification_script.py -p 21 80 3389 3306
```
### Help

To see all available arguments and their descriptions, run the script with the `-h` flag:

```bash
python port_identification_script.py -h
```
