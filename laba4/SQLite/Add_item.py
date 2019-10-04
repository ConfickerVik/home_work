
class Preparation:
    # Функция создания таблиц БД
    def createTable(self, conn, cursor):

        cursor.execute("CREATE TABLE Discipline (id INTEGER PRIMARY KEY, discipline_name string)")
        cursor.execute("CREATE TABLE Teacher (id INTEGER PRIMARY KEY, name string, patronymic string,second_name string)")
        cursor.execute("CREATE TABLE Weekday (id INTEGER PRIMARY KEY, weekday_name string)")
        cursor.execute("CREATE TABLE Audience (id INTEGER PRIMARY KEY, audience_name string)")
        cursor.execute("CREATE TABLE CountLecture (id INTEGER PRIMARY KEY, count_lec string)")
        cursor.execute("CREATE TABLE CountStudent (id INTEGER PRIMARY KEY, count_stud string)")

    # Функция добавление предварительных данных в БД
    def AddItemTable(self, conn, cursor):
        discipline = [(1, 'Программная инженерия'),
                      (2, 'Конструирование программного обеспечения'),
                      (3, 'Алгоритмы и структуры данных'),
                      (4, 'Программирование'),
                      (5, 'Тестирование')]
        teacher = [(1, 'Ощепков', 'Виктор', 'Анатольевич'),
                   (2, 'Хмелев', 'Иван', 'Николаевич'),
                   (3, 'Сафонов', 'Сергей', 'Викторович'),
                   (4, 'Трофимов', 'Евгений', 'Сергеевич'),
                   (5, 'Морина', 'Лидия', 'Вячеславовна')]
        weekday = [(1, 'Понедельник'),
                   (2, 'Вторник'),
                   (3, 'Среда'),
                   (4, 'Четверг'),
                   (5, 'Пятница')]
        audience = [(1, 'Д514'), (2, 'А218'), (3, 'Б334'), (4, 'Г222'), (5, 'Д303')]
        countlecture = [(1, '1'), (2, '2'), (3, '3'), (4, '2'), (5, '1')]
        countstudent = [(1, '23'), (2, '25'), (3, '17'), (4, '29'), (5, '21')]

        cursor.executemany("INSERT INTO Discipline VALUES (?, ?)", discipline)
        cursor.executemany("INSERT INTO Teacher VALUES (?, ?, ?, ?)", teacher)
        cursor.executemany("INSERT INTO Weekday VALUES (?, ?)", weekday)
        cursor.executemany("INSERT INTO Audience VALUES (?, ?)", audience)
        cursor.executemany("INSERT INTO CountLecture VALUES (?, ?)", countlecture)
        cursor.executemany("INSERT INTO CountStudent VALUES (?, ?)", countstudent)

        conn.commit()
