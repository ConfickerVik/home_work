from laba6.mission6_2.Marshallization import Marshaller


class POJO(object):
    # Инициализация тегов
    def __init__(self):
        self.name = ''
        self.weekday = ''
        self.audience = ''
        self.fullname = ''
        self.disciplineteacher = ''
        self.countdiscipline = ''
        self.countstudent = ''

    # функция для возврата значения по тегу name
    @property
    def get_name(self):
        return self.name

    # функция для присваивания значения тега name
    @get_name.setter
    def get_name(self, value):
        self.name = value

    # функция для возврата значения по тегу weekday
    @property
    def get_weekday(self):
        return self.weekday

    # функция для присваивания значения тега weekday
    @get_weekday.setter
    def get_weekday(self, value):
        self.weekday = value

    # функция для возврата значения по тегу audience
    @property
    def get_audience(self):
        return self.audience

    # функция для присваивания значения тега audience
    @get_audience.setter
    def get_audience(self, value):
        self.audience = value

    # функция для возврата значения по тегу fullname
    @property
    def get_fullname(self):
        return self.fullname

    # функция для присваивания значения тега fullname
    @get_fullname.setter
    def get_fullname(self, value):
        self.fullname = value

    # функция для возврата значения по тегу disciplineteacher
    @property
    def get_disciplineteacher(self):
        return self.disciplineteacher

    # функция для присваивания значения тега disciplineteacher
    @get_disciplineteacher.setter
    def get_disciplineteacher(self, value):
        self.disciplineteacher = value

    # функция для возврата значения по тегу countdiscipline
    @property
    def get_countdiscipline(self):
        return self.countdiscipline

    # функция для присваивания значения тега countdiscipline
    @get_countdiscipline.setter
    def get_countdiscipline(self, value):
        self.countdiscipline = value

    # функция для возврата значения по тегу countstudent
    @property
    def get_countstudent(self):
        return self.countstudent

    # функция для присваивания значения тега countstudent
    @get_countstudent.setter
    def get_countstudent(self, value):
        self.countstudent = value

    # собираем все значения тегов по предметам
    def toStringDiscipline(self):
        print("Class Pojo [name = " + self.name + ", weekday = " + self.weekday + ", audience = " + self.audience + "]")

    # собираем все значения тегов по преподавателям
    def toStringTeacher(self):
        print(
            "Class Pojo [disciplineteacher = " + self.disciplineteacher + ", countdiscipline = " + self.countdiscipline + ", countstudent = " + self.countstudent + ", fullname = " + self.fullname + "]")


if __name__ == '__main__':
    p = POJO()
    p.get_name = 'Программная инженерия'
    p.get_weekday = 'Вторник'
    p.get_audience = 'Д514'
    p.get_fullname = 'Ощепков Виктор Анатольевич'
    p.get_disciplineteacher = 'Программная инженерия'
    p.get_countdiscipline = '1'
    p.get_countstudent = '15'

    print("\nПолученный POJO класс: ")
    p.toStringDiscipline()
    p.toStringTeacher()
    print("*" * 35)

    # название xml файла куда будем преобразовывать объект
    file = "marsh.xml"
    # вызываем класс маршаллизации/демаршаллизации
    m = Marshaller()
    # вызываем маршализацию
    m.marshaller(p, file)

    print("\nПроводим демаршаллизацию:")
    # вызываем демаршаллизацию
    m.unmarshaller(file)
