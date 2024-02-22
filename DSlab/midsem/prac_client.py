import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 12346

sock.connect((HOST,PORT))

data = int(input("Enter number: "))
data = str(data)
sock.sendall(data.encode())
print("waiting for answer")

data = sock.recv(1024)
print("server: ",data.decode())
sock.close()