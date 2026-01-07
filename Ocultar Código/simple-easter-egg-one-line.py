import socket;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('localhost', 9199));s.sendall(b'hello world')
