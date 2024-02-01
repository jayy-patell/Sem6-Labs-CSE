import socket

HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 2053 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(b'Hello World')  # b makes the string a bytes-like object
	data = s.recv(1024)
	print('Received Connection')
	print('Server:', data.decode())  # decode() why??