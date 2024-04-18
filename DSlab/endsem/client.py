import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST=socket.gethostname()
PORT=12345

sock.connect((HOST,PORT))

string = input("Enter string: ")

sock.send(string.encode())
data1 = sock.recv(1024).decode()
data2 = sock.recv(1024).decode()
print(data1)
print(data2)
lst1 = data1.split(",")
lst2 = data2.split(",")

print(lst1)
print(lst2)

sock.close()

