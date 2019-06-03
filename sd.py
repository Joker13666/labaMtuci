import socket

HOST = input('Введите HOST ')
PORT = 8080

user = socket.socket()
user.connect((HOST,PORT))

print(user.recv(1024).decode())

b = input('Введите матрицу в виде "[1 2; 3 4]" ')
user.send(b.encode())

print(user.recv(65565).decode())
user.close()
