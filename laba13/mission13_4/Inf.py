import xml.etree.ElementTree as xml


class Inf:

    def inf(self, file):

            # Парсинг xml-файла
            tree = xml.parse(file)
            # Получение основного тега
            main_tag = tree.getroot()
            # Получение остальных тегов
            tag = main_tag.getchildren()

            # Объявление тегов
            operation = ''
            inputq = ''
            outputq = ''

            # Перебор элементов основного тега
            for i in tag:
                print(i)
                # Получение дочернего тега
                element = i.getchildren()

                # Перебор элементов дочерних тегов
                for q in element:
                    # Присвоение переменным значения тегов
                    # Если тег = 'operation'
                    if q.tag == "operation":
                        # Получение текста тега
                        operation = q.text
                    el = q.getchildren()

                    for w in el:
                        # Если тег = 'input'
                        if w.tag == "input":
                            # Получение текста тега
                            inputq = w.text
                        # Если тег = 'output'
                        elif w.tag == "output":
                            # Получение текста тега
                            outputq = w.text

            # Вывод в консоль полученных данных
            print("operation = " + operation + "\ninput = " + inputq + ",\noutput = " + outputq)
