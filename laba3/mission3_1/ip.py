import socket
from netaddr import *
import threading


def port_scan(port, host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        connection = s.connect((host, port))
        print(host, 'Port :', port, "is open.\n")
        connection.close()
    except:
        pass


ipStart, ipEnd = input("Введите диапозон IP адрессов для сканирования: ").split("-")
iprange = IPRange(ipStart, ipEnd)

port = int(input('Введите порт: '))

for ip in iprange:
    host = str(ip)
    t = threading.Thread(target=port_scan, args=(port, host))
    t.start()
