#!/usr/bin/python3
import socket

def port_scanner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        return True
    except:
        return False

host = input("Enter the host to scan: ")

for port in range(1, 65535):
    if port_scanner(host, port):
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed or blocked")
