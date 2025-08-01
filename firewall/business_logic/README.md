# Methods to Simulate the Firewall

- This page provides a list of methods to simulate various types of attacks on the Python-based firewall. These simulations are useful for testing the firewall's ability to detect and block malicious activities.
- Suggests to generate simulations from another machine (preferably Linux OS based). However, apply command prompt in administrator mode with directory and command. Likewise using Kali Linux Virtual Machine instead (e.g. if the <hping3> is not working in Windows).


-----------------------------------------------------------------------------------------------------------------------------------

## 1. Port Scanning
- **Purpose**: Simulate scanning for open ports to test port scanning detection.

  - Use tools like `nmap` or `hping3` to scan ports on the target IP.
  - Example Command (using `nmap`):
    
    "nmap -p 1-1000 <target ip>" or "nmap -Pn <target ip>"
    
  - Example Command (using `hping3`):
    
    "hping3 -S -p ++1 <target ip>"
    
-----------------------------------------------------------------------------------------------------------------------------------

## 2. High Packet Rate (Flooding)
- **Purpose**: Simulate a denial-of-service (DoS) attack by sending packets at a high rate.

  - Use `hping3` to flood the target with packets.
  - Example Command

    "hping3 -c 1000 -d 120 -S -w 64 -p 80 --flood <target ip>"

-----------------------------------------------------------------------------------------------------------------------------------

## 3. ICMP (Ping) Flood
- **Purpose**: Simulate an ICMP flood attack to test ICMP blocking by port to port.

  - Use `hping3` to send ICMP packets to the target.
  - Example Command:
    
    "hping3 -1 --flood <target ip>"
    
-----------------------------------------------------------------------------------------------------------------------------------

## 4. Traffic on Blocked Ports
- **Purpose**: Test if the firewall blocks traffic on specific ports.

  - Use `hping3` to send packets to a blocked port (e.g. port 23).
  - Example Command:
    
    "hping3 -S -p 23 <target ip>"

-----------------------------------------------------------------------------------------------------------------------------------

## 5. Traffic on UDP
- **Purpose**: Test if the firewall allows traffic on UDP.

  - Use `hping3` to send packets to trigger UDP function (e.g. port 443).
  - Example Command:
    
    "hping3 -2 -p 23 <target ip>"
    
-----------------------------------------------------------------------------------------------------------------------------------
## 6. Traffic on Whitelisted Ports
- **Purpose**: Test if the firewall allows traffic on whitelisted ports.

  - Use `hping3` to send packets to a whitelisted port (e.g. port 443).
  - Example Command:
    
    "hping3 -S -p 443 <target ip>"
    
-----------------------------------------------------------------------------------------------------------------------------------

## 7. Repeated Connection Attempts `repeated_connection_attempts` 
- **Purpose**: Simulate repeated connection attempts to test connection rate limiting.

  - Example Command

    "python repeated_connection_attempts.py <target_ip> <target_port> -a <attempts> -d <delay>"

-----------------------------------------------------------------------------------------------------------------------------------

## 8. Simulate Port Scanning with `port_scanner.py`
- **Purpose**: Use the `port_scanner.py` script from business_logic folder to simulate port scanning.

  - Run the script to scan ports on the target IP.
  - Example Command:
    
    "python port_scanner.py <target ip> 20 100"

-----------------------------------------------------------------------------------------------------------------------------------

## 9. Simulate Brute Force with `ping.py`
- **Purpose**: Use the `ping.py` script from business_logic folder to simulate repeated ICMP requests.

  - Run the script to send multiple ping requests to the target IP.
  - Example Command:
    
    "python ping.py <target ip> -c 100"
    
-----------------------------------------------------------------------------------------------------------------------------------

## Notes
- Perform these simulations in a **controlled environment** to avoid disrupting real systems.
- Monitor the firewall logs (`firewall.log`) to verify its response to each attack.
- Adjust thresholds in `config.json` (e.g., `threat_threshold`, `scan_threshold`) to fine-tune detection sensitivity.

-----------------------------------------------------------------------------------------------------------------------------------