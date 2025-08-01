import socket
import argparse
import time

def repeated_connection_attempts(target_ip, target_port, attempts, delay):
    """
    Simulates repeated connection attempts to a specific port on the target IP.

    Args:
        target_ip (str): The target IP address.
        target_port (int): The target port number.
        attempts (int): Number of connection attempts.
        delay (float): Delay (in seconds) between each attempt.
    """
    print(f"Starting repeated connection attempts to {target_ip}:{target_port}")
    for i in range(attempts):
        try:
            # Create a socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Set timeout for the connection
            s.connect((target_ip, target_port))  # Attempt to connect
            s.close()  # Close the connection
            print(f"Attempt {i + 1}: Connection successful")
        except socket.timeout:
            print(f"Attempt {i + 1}: Connection failed - Timed out")
        except ConnectionRefusedError:
            print(f"Attempt {i + 1}: Connection failed - Connection refused")
        except Exception as e:
            print(f"Attempt {i + 1}: Connection failed - {e}")
        time.sleep(delay)  # Wait before the next attempt
    print("Repeated connection attempts completed.")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Simulate repeated connection attempts to test the firewall.")
    parser.add_argument("target_ip", help="Target IP address to connect to")
    parser.add_argument("target_port", type=int, help="Target port number to connect to")
    parser.add_argument("-a", "--attempts", type=int, default=100, help="Number of connection attempts (default: 100)")
    parser.add_argument("-d", "--delay", type=float, default=0.1, help="Delay (in seconds) between attempts (default: 0.1)")
    args = parser.parse_args()

    # Run the repeated connection attempts
    repeated_connection_attempts(args.target_ip, args.target_port, args.attempts, args.delay)