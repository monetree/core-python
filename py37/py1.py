#file server
import socket
s = socket.socket()
host = 'localhost'
port = 9999
s.bind((host,port))
s.listen(1)
c, addr = s.accept()
print('client connection from ', addr)
fname = c.recv(1024)
fname = fname.decode()
print('filename receieved= ', fname)
try:
    f = open(fname, 'rb')
    data = f.read()
    c.send(data)
    f.close()
    print('file data sent to the client')
except FileNotFoundError:
    c.send(b'file does not exist !')
c.close()
s.close()

