#!/usr/bin/python
#coding=utf-8
import socket
HOST = '127.0.0.1'    # 远程主机IP
PORT = 50007              # 远程主机端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('456') # 发送数据
data = s.recv(1024)       # 接收服务端发来的数据
s.close()
print('Received: ', data)