#!/usr/bin/python3
import sys
import time
import socket
import threading

usage = "Usage: python3 NetworkScanner.py <target> -p <start port> <end port> -t <threads>"

# Ensure the right number of arguments
if len(sys.argv) != 7:
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

try:
    stport = int(sys.argv[3])
    edport = int(sys.argv[4])
    threads_count = int(sys.argv[6])
except ValueError:
    print("Invalid port or thread input")
    sys.exit()

# Validate port range and threads
if stport < 1 or edport > 65535 or stport > edport:
    print("Invalid port range. Ports must be between 1 and 65535.")
    sys.exit()

if threads_count < 1:
    print("Number of threads should be at least 1.")
    sys.exit()

# Time the scan
sttime = time.time()

# Function to grab banner and try identifying the service
def grab_banner(s):
    try:
        return s.recv(1024).decode().strip()
    except:
        return "Unknown Service/Banner"

# Function to scan a port and try to detect the service
def start_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        conn = s.connect_ex((target, port))
        if conn == 0:
            print(f"Port {port} is open", end="")
            try:
                # Attempt to grab a service banner
                s.send(b'HEAD / HTTP/1.1\r\n\r\n')
                banner = grab_banner(s)
                if banner:
                    print(f" - Service: {banner}")
                else:
                    print(f" - Service: Unknown")
            except Exception as e:
                print(f" - Unable to detect service: {e}")
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# List to hold threads
threads = []

# Launch threads
for port in range(stport, edport + 1):
    thread = threading.Thread(target=start_scan, args=(port,))
    threads.append(thread)
    thread.start()

    # Limit the number of threads running concurrently
    if len(threads) >= threads_count:
        for t in threads:
            t.join()  # Wait for all threads to complete
        threads = []  # Reset the list for new threads

# Ensure any remaining threads are joined
for t in threads:
    t.join()

# Calculate elapsed time
edtime = time.time()
print("Time to complete:", edtime - sttime)

sys.exit()
