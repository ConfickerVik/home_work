import socket
import sys

sock = socket.socket()
ip = input("Введите ip адрес: ")
port = int(input("Введите порт: "))
sock.connect((ip, port))
while True:
    message = input("Введите сообщение!: ")
    if message == 'exit':
        sock.send(message.encode())
        print('До свидания!')
        sock.close()
        sys.exit()
    else:
        sock.send(message.encode())
        print(sock.recv(1024).decode())
        
