# 1. Write a UDP time server to display the current time and day.

import socket
import time
from datetime import date

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # For UDP
udp_host = socket.gethostname() # Host IP
udp_port = 12345 # specified port to connect

sock.bind((udp_host, udp_port))


print("Waiting for client...")
data,addr = sock.recvfrom(1024)
currentTime = time.ctime(time.time()) + "\r\n"
sock.sendto(str(currentTime).encode('ascii'),addr)
dateAsString = str(date.today())
sock.sendto(dateAsString.encode(),addr)

sock.close()