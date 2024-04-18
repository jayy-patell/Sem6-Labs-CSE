import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#HOST='localhost'
HOST=socket.gethostname()
PORT=12345

sock.bind((HOST,PORT))
sock.listen(1)

print("TCP server has started and is ready to recieve")
conn,addr = sock.accept()

data = conn.recv(1024).decode()
print(data)

str_lst = data.strip().split()
num_lst = []
char_lst = []

for word in str_lst:
    for char in word:
        if char>='0' and char<='9':
            num_lst.append(char)
        else:
            char_lst.append(char)

print(num_lst)
print(char_lst)

st = ",".join(num_lst)
st1 = ",".join(char_lst)
conn.send(st.encode())
conn.send(st1.encode())

sock.close()