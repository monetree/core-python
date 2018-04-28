#A file client
import socket
host = 'localhost'
port = 9999
s = socket.socket()
s.connect((host,port))
fname = input("enter file name: ")
fname = fname.encode()
s.send(fname)
data = s.recv(1024)
while data:
    print(data.decode())
    data = s.recv(1024)
s.close()
