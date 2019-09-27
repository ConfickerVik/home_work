import socket
import random


def open_file():
    file = ''
    try:
        file = open('Sonets.txt', 'r')
        sonnets = file.read().split('*')
        return sonnets
    except Exception:
        print("Error!")
    finally:
        file.close()


def getSonnet():
    get = open_file()
    return random.choice(get)

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
        sonnet = getSonnet()
        conn.send(sonnet.encode())

conn.close()
