Network Monitor Tool
====================

Overview
--------

The Network Monitor Tool is a Python-based utility designed to monitor devices on your WiFi network and capture network traffic. It provides basic functionality for discovering connected devices and capturing/analyzing network traffic.

Features
--------

-   Discover all devices connected to your network.
-   Capture and analyze network traffic.
-   Display relevant information about network packets.

Prerequisites
-------------

-   Python 3.x
-   Pip (Python package installer)

Installation
------------

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

sh


`git clone https://github.com/yourusername/network-monitor-tool.git
cd network-monitor-tool`

### Step 2: Install Dependencies

Install the required Python libraries using pip:

sh



`pip install scapy psutil`

Usage
-----

1.  Open a terminal and navigate to the directory where you cloned the repository.

2.  Run the network monitoring tool:

sh



`python network_monitor.py`

1.  The tool will start by discovering devices on your network and then begin capturing network traffic.

Code Overview
-------------

### `network_monitor.py`

This is the main script for the network monitoring tool. Below is an overview of the key components:

#### `NetworkMonitor` Class

-   **`__init__(self)`**: Initializes the NetworkMonitor class.
-   **`get_interfaces(self)`**: Retrieves network interfaces except the loopback interface.
-   **`discover_devices(self)`**: Discovers devices on the network using ARP requests.
-   **`capture_traffic(self, interface)`**: Captures network traffic on a specified interface.
-   **`process_packet(self, packet)`**: Processes and displays packet information.
-   **`start_monitoring(self)`**: Starts monitoring by capturing traffic on all network interfaces.

### Example Code

Here's the main part of the `network_monitor.py` script:

python


```
import scapy.all as scapy
import psutil
import socket
import threading

class NetworkMonitor:
    def __init__(self):
        self.devices = []

    def get_interfaces(self):
        interfaces = psutil.net_if_addrs()
        return [i for i in interfaces if i != 'lo']

    def discover_devices(self):
        interfaces = self.get_interfaces()
        for interface in interfaces:
            print(f"Scanning on interface: {interface}")
            scapy.arping("192.168.1.0/24")  # Adjust the subnet as necessary

    def capture_traffic(self, interface):
        scapy.sniff(iface=interface, prn=self.process_packet, store=False)

    def process_packet(self, packet):
        print(packet.show())  # Customize this to extract and display relevant info

    def start_monitoring(self):
        interfaces = self.get_interfaces()
        for interface in interfaces:
            thread = threading.Thread(target=self.capture_traffic, args=(interface,))
            thread.start()

if __name__ == "__main__":
    monitor = NetworkMonitor()
    monitor.discover_devices()
    monitor.start_monitoring()
```

Customization
-------------

### Subnet Adjustment

-   Modify the subnet in the `scapy.arping("192.168.1.0/24")` line according to your network configuration.

### Packet Processing

-   Customize the `process_packet` method to extract and display the specific information you need from the captured packets.

### Extending the Tool

-   Consider adding a GUI or web interface for a more user-friendly experience.
-   Store captured data in a database for later analysis.
-   Implement advanced packet inspection to identify applications, protocols, and potential security issues.

About Me
------------
- I'm Brian Ndegwa, a passionate IT professional with over 5 years of experience.
- I specialize in cybersecurity.
- My expertise spans system development, network administration, and penetration testing.
- I'm proficient in C, Python, Java, Django, and React.
- I developed RONA, a nationally recognized virtual assistant to combat misinformation during the pandemic.
- I value collaboration, teamwork, and continuous learning.

Contributing
------------

Feel free to submit issues and pull requests. Contributions are welcome!

License
-------

This project is licensed under the MIT License.
