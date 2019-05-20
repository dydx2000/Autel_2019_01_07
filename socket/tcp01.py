#coding:utf-8
import socket
host = ''
port = 50007
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn,addr = s.accept()
print('Connected by',addr)
while 1:
    data = conn.recv(1024)
    if not data:break
    print("Received:",data)
    conn.sendall(data)

conn.close()