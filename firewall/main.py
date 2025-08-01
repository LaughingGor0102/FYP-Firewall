import os
import sys
import json
import logging
import argparse
from scapy.all import sniff, IP, TCP, UDP, ICMP
from blocklist_manager import is_blocked_ip, is_blocked_port, add_ip, add_port, save_blocklist
from rate_limiter import detect_threat
from port_scan_tracker import is_port_scanning
from whitelist_manager import is_whitelisted, add_ip_to_whitelist, save_whitelist, WHITELISTED_PORTS
from centralised_logging import setup_logging

# Logger Setup
logger = setup_logging()

# Load configuration from config.json
def load_config():
    config_file = "config.json"
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        logger.error(f"Configuration file {config_file} not found.")
        sys.exit(1)

# Packet Handler
def packet_handler(packet):
    try:
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst

            # Only process packets destined for the target IP
            if ip_dst != target_ip:
                return  # Ignore packets not destined for the target machine
            
            # Check whitelist
            if is_whitelisted(ip_src):
                logger.info(f"Allowed packet from whitelisted IP: {ip_src}")
                print(f"[INFO] Allowed packet from whitelisted IP: {ip_src}")
                return  # Allow the packet

            # Detect threats
            if detect_threat(ip_src):
                logger.warning(f"Threat detected from IP: {ip_src}. Blocking traffic.")
                print(f"[WARNING] Threat detected from IP: {ip_src}. Blocking traffic.")
                return

            # Check blocklist
            if is_blocked_ip(ip_src):
                logger.info(f"Blocked packet from blacklisted IP: {ip_src}")
                print(f"[BLOCKED] Packet from blacklisted IP: {ip_src}")
                return  # Drop the packet

            # Block ICMP (PING) packets
            if ICMP in packet:
                logger.info(f"Blocked ICMP packet (PING) from {ip_src} to {ip_dst}")
                print(f"[BLOCKED] ICMP packet (PING) from {ip_src} to {ip_dst}")
                return  # Drop the packet

            # Handle UDP packets
            if UDP in packet:
                sport = packet[UDP].sport
                dport = packet[UDP].dport

                # Check blocklist for ports
                if is_blocked_port(sport) or is_blocked_port(dport):
                    logger.info(f"Blocked UDP packet on blacklisted port: {sport}->{dport} from {ip_src} to {ip_dst}")
                    print(f"[BLOCKED] UDP packet on blacklisted port: {sport}->{dport} from {ip_src} to {ip_dst}")
                    return  # Drop the packet

            # Handle TCP packets
            if TCP in packet:
                sport = packet[TCP].sport
                dport = packet[TCP].dport

                # Detect port scanning
                if is_port_scanning(ip_src, dport):
                    logger.info(f"Blocked port scanning attempt from {ip_src}")
                    add_ip(ip_src)  # Add the IP to the blocklist
                    save_blocklist()  # Save the updated blocklist
                    print(f"[BLOCKED] Port scanning attempt from {ip_src}")
                    return  # Drop the packet

                # Check whitelist for ports
                if is_whitelisted(ip_src, sport) or is_whitelisted(ip_src, dport):
                    logger.info(f"Allowed packet on whitelisted port: {sport}->{dport} from {ip_src} to {ip_dst}")
                    print(f"[INFO] Allowed packet on whitelisted port: {sport}->{dport} from {ip_src} to {ip_dst}")
                    return  # Allow the packet

                # Check blocklist for ports
                if is_blocked_port(sport) or is_blocked_port(dport):
                    logger.info(f"Blocked packet on blacklisted port: {sport}->{dport} from {ip_src} to {ip_dst}")
                    print(f"[BLOCKED] Packet on blacklisted port: {sport}->{dport} from {ip_src} to {ip_dst}")
                    return  # Drop the packet

            # Allow and log
            logger.info(f"Allowed packet from {ip_src} to {ip_dst}")
            print(f"[INFO] Allowed packet from {ip_src} to {ip_dst}")

    except Exception as e:
        logger.error(f"Error processing packet: {e}")
        print(f"[ERROR] Error processing packet: {e}")

# Start Sniffing
def start_firewall():
    print("Firewall is running... Press Ctrl+C to stop.")
    sniff(prn=packet_handler, store=0)

if __name__ == "__main__":
    # Load configuration
    config = load_config()

    # Set target IP and other configurations
    target_ip = config["target_ip"]

    # Initialize blocklists and whitelists
    for ip in config["blocked_ips"]:
        add_ip(ip)
    for port in config["blocked_ports"]:
        add_port(port)
    for ip in config["whitelisted_ips"]:
        add_ip_to_whitelist(ip)
    for port in config["whitelisted_ports"]:
        WHITELISTED_PORTS.add(port)

    print(f"Starting firewall for target IP: {target_ip}")
    logger.info("Firewall started.")
    start_firewall()