class Request:
    def first_request(self, curs):
        day = input("Введите день недели (Пример: 'Понедельник'): ")
        audience = input("Введите номер кабинета (Пример: 'Д567'): ")
        sql = "SELECT * " \
              "FROM Teacher" \
              "INNER JOIN Weekday ON Teacher.id = Weekday.id " \
              "INNER JOIN Audience ON Teacher.id = Audience.id" \
              "WHERE Weekday.weekday_name = %s AND Audience.audience_name = %s" % (day, audience)
        curs.execute(sql)
        return curs.fetchall()

    def second_request(self, curs):
        day = input("Введите день недели (Пример: 'понедельник'): ")
        sql = "SELECT * " \
              "FROM Teacher " \
              "INNER JOIN Weekday ON Teacher.id <> Weekday.id " \
              "WHERE Weekday.weekday_name <> %s" % day
        curs.execute(sql)
        return curs.fetchall()

    def third_request(self, curs):
        count = "Введите кол-во занятий (Пример: '2'): "
        sql = "SELECT * " \
              "FROM Weekday" \
              "INNER JOIN CountLecture ON Weekday.id = CountLecture.id " \
              "WHERE CountLecture.count_lec = %s" % count
        curs.execute(sql)
        return curs.fetchall()

    def fourth_request(self, curs):
        count = "Введите кол-во аудиторий (Пример: '2'): "
        sql = "SELECT *" \
              "FROM Weekday" \
              "INNER JOIN CountLecture ON Weekday.id <> CountLecture.id " \
              "WHERE CountLecture.count_lec = %s" % count
        curs.execute(sql)
        return curs.fetchall()

    def fifth_request(self, curs):
        sql = ""
        curs.execute(sql)
        return curs.fetchall()