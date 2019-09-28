import socket
import random


def getstr():
    answer = ['К сожалению, в отпуске плохая погода бывает не только в выходные.',
        'Пыль и батарейки садятся без приглашения.',
        'Еще немного и я не выдержу и возьму кредит на фисташки.',
        'Успех пришел по глупости, ушел - по идиотски.',
        'В пиве в 2 раза меньше сахара чем в соке. Как вам такое здоровое питание?',
        'Python - лучший язык программирования.']
    return random.choice(answer)

sock = socket.socket()
sock.bind(('', 22))
sock.listen(10)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    else:
        mes = getstr()
        conn.send(mes.encode())

conn.close()
