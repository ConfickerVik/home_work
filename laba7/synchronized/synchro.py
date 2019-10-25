import threading
import time
import random

semaphore = threading.Semaphore(0)


def tunnel():
    print("Туннель свободен!")
    semaphore.acquire()
    print(f"Поезд прошёл за {item} секунд(ы)")


def train():
    global item
    item = random.randint(0, 10) + 1
    print("Поезд заехал в туннель! Ожидание")
    time.sleep(item)
    semaphore.release()


if __name__ == '__main__':
    for i in range(10):
        t1 = threading.Thread(target=tunnel)
        tr = threading.Thread(target=train)
        t1.start()
        tr.start()
        t1.join()
        tr.join()
    print("Finish.")
