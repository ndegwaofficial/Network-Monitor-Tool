"""
Network Monitor Tool

Author: Brian Ndegwa

Overview:
The Network Monitor Tool is a Python-based utility designed to monitor devices on your WiFi network and capture network traffic. It provides basic functionality for discovering connected devices and capturing/analyzing network traffic.

Features:
- Discover all devices connected to your network.
- Capture and analyze network traffic.
- Display relevant information about network packets.

License: MIT License
"""

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
