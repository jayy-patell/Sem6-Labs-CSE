# 1A) Write a program where client can send a message to the server and the server can receive
# the message and send, or echo, it back to the client.
# 172.16.58.255
import socket

HOST = "127.0.0.1" # Standard loopback interface address (localhost)
PORT = 2053 # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()

	with conn:
		print("Connected by ", addr)
		while True:
			data = conn.recv(1024)
			if data:
				print("Client: ", data.decode())
			data = input("Enter message to client: ")
			if not data:
				break
			# sending message as bytes to client
			conn.sendall(bytearray(data,'utf-8'))

	conn.close()