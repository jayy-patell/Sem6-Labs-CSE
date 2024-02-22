
def digsum(num):
    sum=0
    while num>0:
        d=num%10
        sum=sum+d
        num=num//10
    return sum


import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 12346

sock.bind((HOST,PORT))
sock.listen(1)

conn,addr = sock.accept()
print("connected to: ",addr[0])
data = conn.recv(1024)
print("After recieving: ",data.decode())

num = int(data.decode())
sum = digsum(num)

print(f"Before sending: {sum}")
conn.sendall(str(sum).encode())
conn.close()
