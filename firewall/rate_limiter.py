from collections import defaultdict
from blocklist_manager import add_ip
import time 

THREAT_THRESHOLD = 20  # Number of packets per second considered a threat
threat_tracker = defaultdict(list)

def detect_threat(ip):
    current_time = time.time()
    threat_tracker[ip] = [t for t in threat_tracker[ip] if current_time - t < 1]
    threat_tracker[ip].append(current_time)
    if len(threat_tracker[ip]) > THREAT_THRESHOLD:
        add_ip(ip)  # Dynamically block the IP
        return True
    return False
