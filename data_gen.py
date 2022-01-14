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
                           'HTTP': 80,
                           'HTTPv1': 7980,
                           'HTTPv2': 8080,
                           'psql': 5432,
                           'HTTPS': 443,
                           'SMTP': 25,
                           'ICMP': 7,
                           'HDFS': 9870,
                           'DHCP': 51}
        self.ip_range = {'client': "191.168.21.132",
                         'client2': "191.168.21.142",
                         'client3': "191.168.21.135",
                         'HDFS Server': "192.168.21.200",
                         'Web_app_Server': "192.168.21.50",
                         'psql&Web': "192.168.21.10",
                         'DHCP_Server': "192.168.21.100"}
        self.data = []
        self.info = {}

    def create_package(self, proto, src_port, dst_ip, dst_port, ip):
        package = Ether() / IP(src=ip, dst=dst_ip)
        if str(proto) == "ICMP":
            package = package / ICMP()
        elif str(proto) == "TCP":
            package = package / TCP(sport=src_port, dport=dst_port)
        elif str(proto) == "UDP":
            package = package / UDP(sport=src_port, dport=dst_port)
        return package

    def ssh_connections(self):
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("TCP", src_port, self.ip_range['psql&Web'], self.port_range['ssh'], self.ip_range['client']))
        src_port = randint(9999, 11111)
        for i in range(self.n+2):
            self.data.append(self.create_package("TCP", src_port, self.ip_range['HDFS Server'], self.port_range['ssh'], self.ip_range['client3']))
        src_port = randint(9999, 11111)
        for i in range(self.n-2):
            self.data.append(self.create_package("TCP", src_port, self.ip_range['client2'], self.port_range['ssh'], self.ip_range['client']))
        src_port = randint(9999, 11111)
        for i in range(self.n+2):
            self.data.append(self.create_package("TCP", src_port, self.ip_range['Web_app_Server'], self.port_range['ssh'], self.ip_range['psql&Web']))
        self.info['ssh'] = self.n*4 + 2

    def WebApp_connections(self):
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("TCP", src_port, self.ip_range['Web_app_Server'], self.port_range['HTTP'], self.ip_range['psql&Web']))
        src_port = randint(9999, 11111)
        for i in range(self.n-2):
            self.data.append(self.create_package("TCP", src_port, self.ip_range['psql&Web'], self.port_range['HTTP'], self.ip_range['client3']))
            self.data.append(self.create_package("TCP", src_port, self.ip_range['psql&Web'], self.port_range['HTTP'], self.ip_range['client']))
#        self.info['Web_app'] = (self.n - 2)*2
        self.info['Web_appv1'] = self.n*2

    def psql_connections(self):
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("TCP", src_port, self.ip_range['psql&Web'], self.port_range['psql'], self.ip_range['Web_app_Server']))
        src_port = randint(9999, 11111)
        for i in range(self.n+2):
            self.data.append(self.create_package("TCP", src_port, self.ip_range['psql&Web'], self.port_range['psql'], self.ip_range['client2']))
        src_port = randint(9999, 11111)
        for i in range(self.n-2):
            self.data.append(self.create_package("TCP", src_port, self.ip_range['psql&Web'], self.port_range['psql'], self.ip_range['client3']))
        self.info['psql'] = self.n*3

    def DHCP_connections(self):
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("UDP", src_port, self.ip_range['DHCP_Server'], self.port_range['DHCP'], self.ip_range['client']))
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("UDP", src_port, self.ip_range['DHCP_Server'], self.port_range['DHCP'], self.ip_range['client2']))
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("UDP", src_port, self.ip_range['DHCP_Server'], self.port_range['DHCP'], self.ip_range['client3']))
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("UDP", src_port, self.ip_range['DHCP_Server'], self.port_range['DHCP'], self.ip_range['HDFS Server']))
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("UDP", src_port, self.ip_range['DHCP_Server'], self.port_range['DHCP'], self.ip_range['psql&Web']))
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("UDP", src_port, self.ip_range['DHCP_Server'], self.port_range['DHCP'], self.ip_range['Web_app_Server']))
        self.info['DHCP'] = self.n*6

    def SMTP_connections(self):
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("TCP", src_port, self.ip_range['DHCP_Server'], self.port_range['SMTP'], self.ip_range['Web_app_Server']))
        src_port = randint(9999, 11111)
        for i in range(self.n+2):
            self.data.append(self.create_package("TCP", src_port, self.ip_range['DHCP_Server'], self.port_range['SMTP'], self.ip_range['client2']))
        src_port = randint(9999, 11111)
        for i in range(self.n-2):
            self.data.append(self.create_package("TCP", src_port, self.ip_range['DHCP_Server'], self.port_range['SMTP'], self.ip_range['HDFS Server']))
        self.info['SMTP'] = self.n*3

    def ICMP_connections(self):
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("ICMP", src_port, self.ip_range['DHCP_Server'], self.port_range['ICMP'], self.ip_range['client']))
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("ICMP", src_port, self.ip_range['DHCP_Server'], self.port_range['ICMP'], self.ip_range['client2']))
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("ICMP", src_port, self.ip_range['DHCP_Server'], self.port_range['ICMP'], self.ip_range['HDFS Server']))
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("ICMP", src_port, self.ip_range['client2'], self.port_range['ICMP'], self.ip_range['psql&Web']))
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("ICMP", src_port, self.ip_range['DHCP_Server'], self.port_range['ICMP'], self.ip_range['psql&Web']))
        src_port = randint(9999, 11111)
        for i in range(self.n):
            self.data.append(self.create_package("ICMP", src_port, self.ip_range['DHCP_Server'], self.port_range['ICMP'], self.ip_range['Web_app_Server']))
        self.info['ICMP'] = self.n*6

    def Simulate_ALL(self):
        self.ICMP_connections()
        self.SMTP_connections()
        self.DHCP_connections()
        self.psql_connections()
        self.WebApp_connections()
        self.ssh_connections()

a = Dataset()
a.Simulate_ALL()
print(type(a.data))
