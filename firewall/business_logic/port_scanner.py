# Port Scanner

import logging
import socket
import argparse

def port_scanner(ip, start_port, end_port):
    logging.info(f"Starting port scan on {ip} from port {start_port} to {end_port}")
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((ip, port)) == 0:
                    open_ports.append(port)
                    logging.info(f"Port {port} is open on {ip}")
                    print(f"Port {port} is open on {ip}")
        except Exception as e:
            logging.error(f"Error scanning port {port} on {ip}: {e}")
    logging.info(f"Port scan complete. Open ports on {ip}: {open_ports}")
    print(f"Port scan complete. Open ports on {ip}: {open_ports}")
    return open_ports

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Scan ports on a target IP address.")
    parser.add_argument("ip", help="Target IP address to scan")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")
    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

    # Run the port scanner
    port_scanner(args.ip, args.start_port, args.end_port)
