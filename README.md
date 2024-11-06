# Network Port Scanner

A powerful command-line network port scanner built in Python for efficiently identifying open and closed ports on specified hosts. This tool provides a simple way to improve network security by auditing available services and ensuring port configurations align with security policies.

## Features

- Scan single or multiple ports on a specified host
- Supports customizable scan ranges
- Displays status of each scanned port (open/closed)
- Fast and efficient scanning using concurrent threads
- User-friendly command-line interface

## Requirements

- Python 3.x or higher

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/network-port-scanner.git
    ```
2. Navigate into the project directory:
    ```bash
    cd network-port-scanner
    ```
## Usage

```bash
python port_scanner.py <hostname> <start_port> <end_port>
```
- `<hostname>`: The IP address or domain name of the target machine
- `<start_port>`: The starting port number for the scan range
- `<end_port>`: The ending port number for the scan range
### Example
```bash
python port_scanner.py 192.168.1.1 20 80
```
This command scans ports 20 through 80 on the target `192.168.1.1`.
## How It Works
The Network Port Scanner works by attempting to establish a connection to each specified port. If a connection is successful, the port is marked as open; otherwise, it is closed.

The scanner uses multithreading to speed up the scan process, especially useful for scanning large port ranges.

## Contributing
Contributions are welcome! If you have ideas for improving this tool, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

This README is tailored for a Python implementation of the network port scanner. Let me know if you'd like to include or modify any details!
