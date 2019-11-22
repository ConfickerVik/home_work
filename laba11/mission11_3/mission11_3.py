class Subject(object):
    """Субъект"""
    def __init__(self):
        self._data = None
        self._observers = set()

    def attach(self, observer):
        # подписаться на оповещение
        if not isinstance(observer, ObserverBase):
            raise TypeError()
        self._observers.add(observer)

    def detach(self, observer):
        # отписаться от оповещения
        self._observers.remove(observer)

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
        self.notify(data)

    def notify(self, data):
        # уведомить всех наблюдателей о событии
        for observer in self._observers:
            observer.update(data)


class ObserverBase(object):
    """Абстрактный наблюдатель"""
    def update(self, data):
        raise NotImplementedError()


class Observer(ObserverBase):
    """Наблюдатель"""
    def __init__(self, name):
        self._name = name

    def update(self, data):
        print('%s: %s' % (self._name, data))


subject = Subject()
subject.attach(Observer('Подписчик 1'))
subject.attach(Observer('Подписчик 2'))
subject.set_data('Ждём новое поступление!')
subject.notify('Новое поступление!')

