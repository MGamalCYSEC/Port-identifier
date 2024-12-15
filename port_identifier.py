import argparse

# Extended dictionary of ports to common services (with commercial and non-commercial use cases)
SERVICE_DATABASE = {
    20: "FTP Data (File Transfer Protocol - Passive mode)",
    21: "FTP Control (File Transfer Protocol - Often used commercially)",
    22: "SSH (Secure Shell - May support commercial servers)",
    23: "Telnet (Unsecured service, avoid in commercial environments)",
    25: "SMTP (Email servers - Often commercial)",
    53: "DNS (Domain Name System - May support commercial websites)",
    67: "DHCP (Dynamic Host Configuration Protocol)",
    69: "TFTP (Trivial File Transfer Protocol)",
    80: "HTTP (Web server - Commercial sites)",
    110: "POP3 (Post Office Protocol - Email service)",
    135: "MS RPC (Microsoft Remote Procedure Call - Often used for Windows services)",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service (Network Basic Input/Output System)",
    143: "IMAP (Internet Message Access Protocol - Email service)",
    161: "SNMP (Simple Network Management Protocol)",
    162: "SNMP Trap",
    443: "HTTPS (Secure web services - Commercial use)",
    445: "Microsoft-DS (Windows file sharing - Commercial use in Windows environments)",
    3306: "MySQL Database (Enterprise/Commercial DBs)",
    3389: "RDP (Remote Desktop Protocol - Commercial or Enterprise use)",
    3700: "HighPort (Non-standard service, could be custom app or service)",
    4848: "GlassFish Admin Console (Java EE server administration)",
    5985: "WinRM (Windows Remote Management - Often commercial use)",
    6379: "Redis (In-memory database store - Commercial use)",
    7000: "Akamai (HTTP-based service)",
    7676: "ActiveMQ (Apache ActiveMQ messaging service)",
    8020: "Hadoop (HDFS - Hadoop Distributed File System)",
    8027: "Hadoop (HBase region server port)",
    8080: "HTTP Proxy or Alternate Web Services (Often Commercial)",
    8181: "WebLogic Admin (Oracle WebLogic Server Administration)",
    8383: "WebLogic (Oracle WebLogic Server)",
    8484: "Jetty HTTP server (Java-based HTTP server)",
    8585: "JBoss (WildFly - JBoss application server)",
    8686: "JMX (Java Management Extensions - For managing and monitoring Java applications)",
    9200: "Elasticsearch (Search engine server - Used for big data analytics)",
    9300: "Elasticsearch (Cluster communication port)",
    47001: "Windows-specific (Could be used by Windows or custom services)",
    49152: "Dynamic or Private Ports (Used for ephemeral connections)",
    49153: "Dynamic or Private Ports (Used for ephemeral connections)",
    49154: "Dynamic or Private Ports (Used for ephemeral connections)",
    49193: "Dynamic or Private Ports (Used for ephemeral connections)",
    49194: "Dynamic or Private Ports (Used for ephemeral connections)",
    49232: "Dynamic or Private Ports (Used for ephemeral connections)",
    49233: "Dynamic or Private Ports (Used for ephemeral connections)",
    49236: "Dynamic or Private Ports (Used for ephemeral connections)",
    5432: "PostgreSQL Database (Commercial database service)",
    5900: "VNC (Virtual Network Computing - Remote Desktop Protocol)",
    6000: "X11 (X Window System - For graphical user interfaces)",
    6379: "Redis (NoSQL database)",
    7000: "Akamai CDN (Content Delivery Network)",
    8080: "HTTP Proxy or Web Server Alternate (Commercial web apps)",
    8888: "Alternate HTTP (Web applications)",
    9200: "Elasticsearch (Search engine service)",
    10000: "Webmin (System administration)",
    11211: "Memcached (Distributed memory caching service)",
    27017: "MongoDB (NoSQL Database)",
    50000: "DB2 (IBM Database)",
    50070: "Hadoop Web UI",
    27015: "Steam (Gaming server)",
    5000: "UPnP (Universal Plug and Play)",
    1433: "MSSQL (Microsoft SQL Server - Common for commercial use)",
    21: "FTP (File Transfer Protocol)",
    137: "NetBIOS (File Sharing)",
    161: "SNMP (Simple Network Management Protocol)",
    3389: "RDP (Remote Desktop Protocol)",
    5432: "PostgreSQL",
    27017: "MongoDB",
    2049: "NFS (Network File System)",
    5050: "ICQ (Instant Messaging Service)",
    8009: "AJP (Apache JServ Protocol)",
    9100: "JetDirect (Printer Protocol)",
    5001: "Dyndns (Dynamic DNS service)",
    12345: "NetBus (Backdoor Trojan)",
    31337: "Back Orifice (Trojan)",
    9999: "Hack attempts (Backdoor ports)",
    11111: "Superscan (Scan ports commonly used by hacking tools)",
    3000: "Node.js (Web framework)",
    4040: "Frame Relay (A protocol used in telecommunications)",
    9000: "SonarQube (Continuous inspection of code quality)",
    10051: "Zabbix (Network Monitoring)",
    23000: "Metasploit (Exploit Framework)",
    20000: "Webmin (System administration)",
    7050: "Unify VoIP (VoIP Protocol)",
    8081: "Tomcat Web Server (Apache Tomcat application server)",
    5038: "Asterisk (VoIP server)",
    2775: "World of Warcraft (Game server port)",
    6003: "X11 (X Window System on display 3)",
    123: "NTP (Network Time Protocol)",
    25565: "Minecraft (Game server port)",
    50: "IPSec (Internet Protocol Security)",
    4455: "Jenkins (CI/CD tool)",
    2010: "Ipswitch IMail (Mail server)",
    1080: "SOCKS Proxy (Proxy service)",
    9998: "Back Orifice (Trojan)",
    12121: "Baidu Cloud (Cloud services)",
    17500: "Dropbox (Cloud storage service)",
    22500: "Dropbox LAN Sync",
    4430: "ADSL (Asymmetric Digital Subscriber Line)",
    5222: "XMPP (Jabber Protocol for instant messaging)",
    8483: "Jetty (HTTP server)",
    9001: "Tor (The Onion Router - Anonymizing network)",
    5631: "PCAnywhere (Remote desktop tool)",
    8088: "WebSocket Service",
    4444: "Metasploit (Exploit framework port)",
    6969: "BitTorrent (P2P sharing protocol)",
    3141: "Pi (Custom Pi-hole DNS service)",
    7070: "Real-Time Streaming Protocol (RTSP)",
    1723: "PPTP (Point-to-Point Tunneling Protocol)",
    28960: "Call of Duty (Game server port)",
    1158: "Twitch (Live streaming)",
    5100: "Blynk (IoT application port)",
    9500: "Cisco (Cisco communications)",
    1443: "HTTPS (Alternate SSL port for web servers)",
    11235: "Asterisk (VoIP server)",
    3388: "RDP (Remote Desktop Protocol - Alternative port)"
}

def identify_ports_from_file(filename):
    """
    Read ports from a file and identify services associated with them.
    
    :param filename: Path to the text file containing ports
    :return: None
    """
    try:
        with open(filename, 'r') as file:
            ports = file.readlines()

        # Clean up and convert ports to integers
        ports = [int(port.strip()) for port in ports if port.strip().isdigit()]

        if not ports:
            print("No valid ports found in the provided file.")
            return

        print("### Port Identification Results ###\n")
        for port in ports:
            service = SERVICE_DATABASE.get(port, "Unknown or non-commercial service")
            print(f"Port {port}: {service}")
    
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def identify_ports_from_input(ports):
    """
    Given a list of ports, identify services associated with them.
    
    :param ports: List of ports to identify
    :return: None
    """
    print("### Port Identification Results ###\n")
    for port in ports:
        service = SERVICE_DATABASE.get(port, "Unknown or non-commercial service")
        print(f"Port {port}: {service}")


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Identify services for given ports"
    )
    
    parser.add_argument('-f', '--file', type=str, help="Path to the text file containing ports")
    parser.add_argument('-p', '--ports', type=int, nargs='*', help="List of ports to identify")

    args = parser.parse_args()

    if args.file:
        identify_ports_from_file(args.file)
    elif args.ports:
        identify_ports_from_input(args.ports)
    else:
        print("No parameters provided. Please provide ports via -f (file) or -p (ports).")


if __name__ == "__main__":
    main()
