from laba4.SQLite import Connect
from laba4.SQLite import Add_item
from laba4.SQLite import Requests
import os
import sys

if __name__ == '__main__':
    file_path = input("Укажите путь до фала БД: ") + '.db'
    if not os.path.exists(file_path):
        con = Connect.ConnectDB()
        connection, session = con.connDB(file_path)
        table = Add_item.Preparation()
        table.createTable(connection, session)
        table.AddItemTable(connection, session)
    else:
        con = Connect.ConnectDB()
        connection, session = con.connDB(file_path)

    list_req = ['1. Вывести информацию о преподавателях, работающих в заданный '
                'день недели в заданной аудитории.',
                '2. Вывести информацию о преподавателях, которые не ведут занятия'
                ' в заданный день недели.',
                '3. Вывести дни недели, в которых проводится заданное количество занятий.',
                '4. Вывести дни недели, в которых занято заданное количество аудиторий.',
                '5. Перенести первые занятия заданных дней недели на последнее место.']
    print("Список запросов: ")
    for i in range(len(list_req)):
        print(list_req[i])


    reque = Requests.Request()
    dict_requests = {
        '1': reque.first_request,
        '2': reque.second_request,
        '3': reque.third_request,
        '4': reque.fourth_request,
        '5': reque.fifth_request
    }
    print('\nВведите номер запроса: ')
    command = input()  # ожидание ввода номера запроса
    if command in dict_requests:  # если номер запроса в словаре
        run = dict_requests[command]  # получаем нужную функцию с запросом
        run(session)
    else:
        print("Ошибочка)")
        sys.exit(0)
