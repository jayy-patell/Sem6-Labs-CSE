import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 12345

sock.connect((HOST,PORT))

# lst=[]
# n = int(input("Enter the number of elements: "))
# for i in range(n):
#     num = input("Enter the number: ")
#     lst.append(num)

# lst = ['121','233','222']

lst = [x for x in input("Enter the numbers: ").split()]

string = ",".join(lst)
print(string)
sock.send(string.encode())

# sock.send(str(lst).encode())
# print(str(lst))



data = sock.recv(1024).decode()
print(data)
data = sock.recv(1024).decode()
print(data)

print("Client: Recieved the result from server")
sock.close()