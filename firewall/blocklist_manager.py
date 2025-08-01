import json
from threading import Lock

BLOCKED_IPS = set()
BLOCKED_PORTS = set()
BLOCKLIST_FILE = "blocklist.json"
lock = Lock()

def add_ip(ip):
    with lock:
        BLOCKED_IPS.add(ip)

def remove_ip(ip):
    with lock:
        BLOCKED_IPS.discard(ip)

def add_port(port):
    with lock:
        BLOCKED_PORTS.add(port)

def remove_port(port):
    with lock:
        BLOCKED_PORTS.discard(port)

def save_blocklist():
    with open(BLOCKLIST_FILE, "w") as f:
        json.dump({"ips": list(BLOCKED_IPS), "ports": list(BLOCKED_PORTS)}, f)

def load_blocklist():
    global BLOCKED_IPS, BLOCKED_PORTS
    try:
        with open(BLOCKLIST_FILE, "r") as f:
            data = json.load(f)
            BLOCKED_IPS = set(data["ips"])
            BLOCKED_PORTS = set(data["ports"])
    except FileNotFoundError:
        pass  

def is_blocked_ip(ip):
    with lock:
        return ip in BLOCKED_IPS
    
def is_blocked_port(port):
    with lock:
        return port in BLOCKED_PORTS