# 4A. Forking/ Threading (Concurrent Server)

import socket
import os
from _thread import *

ServerSocket = socket.socket()

host = '127.0.0.1'
port = 11596

ThreadCount = 0
try:
	ServerSocket.bind((host, port))
except socket.error as e:
	print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)

def threaded_client(connection):
	connection.send(str.encode('Welcome to the Server'))
	while True:
		data = connection.recv(2048)
		print('Received from client :' + str(ThreadCount) +data.decode())
		Inputs = input('Server Says: ')
		if not data:
			break
		connection.sendall(Inputs.encode())
	connection.close()

while True:
	Client, address = ServerSocket.accept()
	print('Connected to: ' + address[0] + ':' + str(address[1]))
	start_new_thread(threaded_client, (Client, ))
	ThreadCount += 1
	print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()


# The function thread.start_new_thread() is used to start a new thread and return its identifier.
# The first argument is the function to call and its second argument is a tuple containing the positional list of arguments.