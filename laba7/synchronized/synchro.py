import logging
import random
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )


class ActiveTonnel(object):
    def __init__(self):
        super(ActiveTonnel, self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Заехал в тонель поезд номер %s', self.active[-1])

    def makeInactive(self, name):
        with self.lock:
            try:
                if len(self.active) == 2:
                    logging.debug('Выехал из тонеля поезд номер %s', self.active[0])
                else:
                    logging.debug('Выехал из тонеля поезд номер %s', self.active[-1])
            except IndexError:
                logging.debug('Поезда закончились, очередь пуста')
            self.active.remove(name)


def train(s, pool):
    logging.debug('Ожидание очереди в тонель')
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)


tonnel = ActiveTonnel()
s = threading.Semaphore(2)
for i in range(1, 11):
    t = threading.Thread(target=train, name=str(i), args=(s, tonnel))
    t.start()

