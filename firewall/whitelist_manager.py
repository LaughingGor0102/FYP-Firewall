import json
from threading import Lock

WHITELISTED_IPS = set()
WHITELISTED_PORTS = set()
WHITELIST_FILE = "whitelist.json"
lock = Lock()

def add_ip_to_whitelist(ip):
    with lock:
        WHITELISTED_IPS.add(ip)

def remove_ip_from_whitelist(ip):
    with lock:
        WHITELISTED_IPS.discard(ip)

def save_whitelist():
    with open(WHITELIST_FILE, "w") as f:
        json.dump({"ips": list(WHITELISTED_IPS), "ports": list(WHITELISTED_PORTS)}, f)

def load_whitelist():
    global WHITELISTED_IPS, WHITELISTED_PORTS
    try:
        with open(WHITELIST_FILE, "r") as f:
            data = json.load(f)
            WHITELISTED_IPS = set(data["ips"])
            WHITELISTED_PORTS = set(data["ports"])
    except FileNotFoundError:
        pass 

# New function to check if an IP or port is whitelisted
def is_whitelisted(ip, port=None):
    with lock:
        if ip in WHITELISTED_IPS:
            return True
        if port and port in WHITELISTED_PORTS:
            return True
    return False