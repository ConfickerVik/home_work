import xml.etree.ElementTree as xml
from lxml import etree
from io import StringIO


class Marshaller:
    # функция маршализации
    def marshaller(self, object, file):
        # создаём главный тег xml-файла
        root = xml.Element("schedule")
        # создаём подтег для главного тега
        appt = xml.Element("classes")
        # добавляем тег в главный тег
        root.append(appt)
        # создаём подтег для предметов и помещаем в classes
        discipline = xml.Element("discipline")
        # добавление тега как подтег
        appt.append(discipline)
        # создаем тег для названия предмета
        name = xml.SubElement(discipline, "name")
        # присваеваем ему значение из объекта POJO
        name.text = object.get_name
        # создаём тег для дня недели
        weekday = xml.SubElement(discipline, "weekday")
        # присваеваем ему значение из объекта POJO
        weekday.text = object.get_weekday
        # создаем тег для аудитории
        audience = xml.SubElement(discipline, "audience")
        # присваеваем ему значение из объекта POJO
        audience.text = object.get_audience
        # создаём подтег для преподавателей и помещаем в classes
        teacher = xml.Element("teacher")
        # добавление тега как подтег
        appt.append(teacher)
        # создаем тег для ФИО
        fullname = xml.SubElement(teacher, "fullname")
        # присваеваем ему значение из объекта POJO
        fullname.text = object.get_fullname
        # создаем тег для предмета, который он преподаёт
        disciplineteacher = xml.SubElement(teacher, "disciplineteacher")
        # присваеваем ему значение из объекта POJO
        disciplineteacher.text = object.get_disciplineteacher
        # создаем тег для количества пар в неделю
        countdiscipline = xml.SubElement(teacher, "countdiscipline")
        # присваеваем ему значение из объекта POJO
        countdiscipline.text = object.get_countdiscipline
        # создаем тег для количества студентов на парах
        countstudent = xml.SubElement(teacher, "countstudent")
        # присваеваем ему значение из объекта POJO
        countstudent.text = object.get_countstudent
        # формируем дерево из списка элементов в root
        tree = xml.ElementTree(root)
        # записываем в файл полученный xml
        with open(file, "w"):
            tree.write(file)

        print("\nМаршаллизация успешно проведена!")

    # Валидация XML по XSD
    def validate(self, filexsd, filexml):
        try:
            # Загрузка XSD файла
            with open(filexsd, 'r') as schema_file:
                schema_to_check = schema_file.read()
            # Парсим нашу схему переведя её в строку
            xmlschema_doc = etree.parse(StringIO(schema_to_check))
            # загружаем нашу схему для проверки
            xmlschema = etree.XMLSchema(xmlschema_doc)
            # проверка валидности xml-файла
            xmlschema.assertValid(filexml)
            print('\nXML valid, schema validation ok.')
            return True

        except etree.DocumentInvalid:
            print('\nSchema validation error')
            exit()

        except:
            print('\nUnknown error, exiting.')
            exit()

    def unmarshaller(self, object, file):
        # храним название нашей схемы
        xsd = "marsh.xsd"
        # создаём объект валидатора
        valid = Marshaller()
        # вызываем валидацию передавая схему и xml-файл
        res = valid.validate(xsd, file)
        if res is True:
            # парсим xml-файл (представляем в виде дерева)
            tree = xml.parse(file)
            # получаем главный тег
            root = tree.getroot()
            # получаем все дочерние теги
            appt = root.getchildren()
            # инициализируем все теги
            name = ''
            weekday = ''
            audience = ''
            fullname = ''
            disciplineteacher = ''
            countdiscipline = ''
            countstudent = ''
            # перебираем все элементы находящиеся в дочерних тегах
            for item in appt:
                # получаем дочерние элементы
                item_children = item.getchildren()
                # перебираем все элементы находящиеся в дочерних тегах
                for item_child in item_children:
                    # получаем дочерние элементы
                    item_child_children = item_child.getchildren()
                    # перебираем все элементы находящиеся в дочерних тегах
                    for item_child_child in item_child_children:
                        # определяем тег и его значение сохраняем
                        if item_child_child.tag == "name":
                            name = item_child_child.text
                        elif item_child_child.tag == "weekday":
                            weekday = item_child_child.text
                        elif item_child_child.tag == "audience":
                            audience = item_child_child.text
                        elif item_child_child.tag == "fullname":
                            fullname = item_child_child.text
                        elif item_child_child.tag == "disciplineteacher":
                            disciplineteacher = item_child_child.text
                        elif item_child_child.tag == "countdiscipline":
                            countdiscipline = item_child_child.text
                        elif item_child_child.tag == "countstudent":
                            countstudent = item_child_child.text
            # формируем новый объект
            object.get_name = name
            object.get_weekday = weekday
            object.get_audience = audience
            object.get_fullname = fullname
            object.get_disciplineteacher = disciplineteacher
            object.get_countdiscipline = countdiscipline
            object.get_countstudent = countstudent
            print("\nДемаршаллизация успешно проведена!")
            return object
        else:
            print("\nОшибка валидации! Демаршаллизация не будет проведена!")
