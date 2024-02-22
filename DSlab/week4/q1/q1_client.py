import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # For UDP
udp_host = socket.gethostname() # Host IP
udp_port = 12345 # specified port to connect

msg = "hello"
s.sendto(msg.encode(),(udp_host,udp_port))

# Receive no more than 1024 bytes
tm,addr = s.recvfrom(1024)
print(' Current time from Sever :', tm.decode())
date,addr = s.recvfrom(1024)
print(' Current day from Sever :', date.decode())
s.close()