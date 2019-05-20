import socket
HOST = '127.0.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data='hello'
s.sendto(data, (HOST, PORT))
data = s.recv(1024)
s.close()
print ('Received: ', data)