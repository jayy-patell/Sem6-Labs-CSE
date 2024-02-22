# import socket

# sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # For UDP
# udp_host = socket.gethostname() # Host IP
# udp_port = 12345 # specified port to connect

# sock.bind((udp_host, udp_port))

# while True:
# 	print("Waiting for client...")
# 	data,addr = sock.recvfrom(1024)
# 	#receive data from client
# 	print ("Received Messages:",data.decode()," from",addr)

import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

HOST=socket.gethostname()
PORT=12345

sock.bind((HOST,PORT))

data,addr = sock.recvfrom(1024)
print("recieved mssg: ",data.decode()," from: ",addr[0])

