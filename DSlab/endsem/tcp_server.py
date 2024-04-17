import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 12345

sock.bind((HOST,PORT))
sock.listen(1)

print("TCP server has started and is ready to recieve")

conn,addr = sock.accept()

lst = conn.recv(1024).decode()
print(type(lst))
print("Server: Recieved data from client: ",lst)

lst = lst.split(',')
print(lst)
for i in range (0,len(lst)):
    lst[i]=int(lst[i])
print(lst)
    
# lst = lst[1:-1].strip().split(',')
# print(type(lst))
# print(lst)

even_sum=0
odd_sum=0
for num in lst:
    sum=0
    temp=int(num)
    while(temp):
        digit=temp%10
        sum+=digit
        temp//=10
    print(sum)
    if sum%2==0:
        even_sum+=sum
    else:
        odd_sum+=sum

print(f"Display the result: {even_sum} {odd_sum}")
conn.send(str(even_sum).encode())
conn.send(str(odd_sum).encode())

sock.close()


