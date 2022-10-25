import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

s.connect((host, port))
while True:
    msg = s.recv(1024)
    if msg != b'':
        print(msg.decode('utf-8'))