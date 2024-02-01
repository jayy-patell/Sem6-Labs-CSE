# 1. Write a UDP time server to display the current time and day.

import socket
import time
from datetime import date

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # For UDP
udp_host = socket.gethostname() # Host IP
udp_port = 12345 # specified port to connect

sock.bind((udp_host, udp_port))

while True:
	print("Waiting for client...")
	currentTime = time.ctime(time.time()) + "\r\n"
	sock.send(currentTime.encode('ascii'))
	dateAsString = str(date.today())
	sock.send(dateAsString.encode())
	sock.close()