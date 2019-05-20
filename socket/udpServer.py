import socket
HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
while 1:
    data, addr = s.recvfrom(1024)
    print ('Connected by', addr)
    print ("Received: ", data)
    s.sendto("Hello %s"% repr(addr), addr)
conn.close()