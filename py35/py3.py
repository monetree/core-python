#A TCP/IP client
import socket
host = 'localhost'
port = 786
s = socket.socket(socket.AF.INET,socket.SOCK_STREAM)
s.connect((host, port))
msg = s.recv(1024)
while msg:
    print(msg)
    msg = s.recv(1024)
s.close()

