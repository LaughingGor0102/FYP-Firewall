from collections import defaultdict
import time
import logging 

SCAN_THRESHOLD = 10  # Number of ports scanned within 1 second
port_scan_tracker = defaultdict(list)

def is_port_scanning(ip, port):
    current_time = time.time()
    port_scan_tracker[ip] = [t for t in port_scan_tracker[ip] if current_time - t[0] < 1]
    port_scan_tracker[ip].append((current_time, port))
    scanned_ports = {entry[1] for entry in port_scan_tracker[ip]}
    if len(scanned_ports) > SCAN_THRESHOLD:
        logging.warning(f"Port scanning detected from IP: {ip}")
        return True
    return False