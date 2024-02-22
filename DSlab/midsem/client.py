import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 12345

sock.connect((HOST,PORT))

num = int(input("Input number: "))
num = str(num)

sock.send(num.encode())
data = sock.recv(1024).decode()

print("Sum of even digits recieved from server: ",str(data))
sock.send(b"Msg from Client: Recieved the sum of even digits. Thank You!")

sock.close()

