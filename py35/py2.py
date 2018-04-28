#A TCP/IP server
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = 'localhost'
port = 786
s.bind((host,port))
s.listen(1)
c, addr = s.accept()
print('A client took connection....')
c.send(b'Hello client')
c.send(b'how are you')
str='bye'
c.send(str.encode())
c.close()
s.close()
