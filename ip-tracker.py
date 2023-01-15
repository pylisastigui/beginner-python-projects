#!/usr/bin/python3
import socket

def ip_tracker(ip):
    try:
        data = socket.gethostbyaddr(ip)
        hostname = data[0]
        location = socket.gethostbyname(hostname)
        return location
    except:
        return "Unable to track location of IP address"

ip = input("Enter the IP address to track: ")
location = ip_tracker(ip)
print("The location of the IP address is: ", location)
