import socket
from time import sleep
HOST=input('Введите имя хоста или айпи адрес: ')
PORT=int(input('Введите порт сервера: '))
sock = socket.socket()
sock.connect((HOST, PORT))

msg = input('Введите ваше сообщение: ')
#msg = "Hi!"
sock.send(msg.encode())

data = sock.recv(1024)
print(data.decode())
sock.close()
