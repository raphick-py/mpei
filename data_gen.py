#!/usr/bin/python

from sys import argv
from time import sleep, time
from random import choice, randint
#from netifaces import AF_INET, ifaddresses
from scapy.all import Ether, IP, TCP, UDP, ICMP
#from importer import RULES


class Dataset:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.n = 10
        self.port_range = {'ssh': 22,
                           'Http': 80,
                           'HTTPv1': 7980,
                           'HTTPv2': 8080,
                           'psql': 5432,
                           'HTTPS': 443,
                           'mail': 25,
                           'HDFS': 9870,
                           'DHCP': 51}
        self.ip_range = {'client': "191.168.21.132",
                         'client2': "191.168.21.142",
                         'client3': "191.168.21.135",
                         'HDFS Server': "192.168.21.100",
                         'Web_app_Server': "192.168.21.50",
                         'psql&Web': "192.168.21.10",
                         'DHCP Server': "192.168.21.2"}

    def create_package(proto, src_port, dst_ip, dst_porti, ip):
        package = Ether() / IP(src=ip, dst=dst_ip)
        if str(proto) == "ICMP":
            package = package / ICMP()
        elif str(proto) == "TCP":
            package = package / TCP(sport=src_port, dport=dst_port)
        elif proto == "UDP":
            package = package / UDP(sport=src_port, dport=dst_port)
        return package

    def ssh_connections():
        for i in range(self.n):
            create_packege(TCP, randint(500, 1000), self.ip_range['psql&Web'], self.port_range['ssh'], self.ip_range['client'])
        for i in range(self.n+2):
            create_packege(TCP, randint(500, 1000), self.ip_range['HDFS Server'], self.port_range['ssh'], self.ip_range['clien3t'])
        for i in range(self.n-2):
            create_packege(TCP, randint(500, 1000), self.ip_range['client2'], self.port_range['ssh'], self.ip_range['client'])

    def WebApp_connections():
        for i in range(self.n):
            create_packege(TCP, randint(500, 1000), self.ip_range['psql&Web'], self.port_range['ssh'], self.ip_range['client'])
        for i in range(self.n+2):
            create_packege(TCP, randint(500, 1000), self.ip_range['HDFS Server'], self.port_range['ssh'], self.ip_range['clien3t'])
        for i in range(self.n-2):
            create_packege(TCP, randint(500, 1000), self.ip_range['client2'], self.port_range['ssh'], self.ip_range['client'])
print(repr(a))
print("===================")
print(a)
