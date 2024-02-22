import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 12345

sock.bind((HOST,PORT))
sock.listen(1)

print("TCP server has started and is ready to recieve")

conn,addr = sock.accept()
num = conn.recv(1024).decode()

print("Server: Recieved data from client: ",str(num))

sum=0
for i in range(len(num)):
	if(int(num[i])%2==0):
		sum+=int(num[i])
print("Display the result: ",str(sum))
conn.send(str(sum).encode())

data = conn.recv(1024)
print(data.decode())

conn.close()
sock.close()

