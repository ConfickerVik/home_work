import socket
import random


def getstr(data):
    get = ['Салам алейкум','Привіт','Dobry den','Konnichi wa','Здаров','Guten Tag']
    return data + random.choice(get)

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(10)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    else:
        mes = getstr(data)
        conn.send(mes.encode())

conn.close()
