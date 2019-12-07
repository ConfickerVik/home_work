import xml.etree.ElementTree as xml


class UnMarshal:

    def unmarshal(self, file):

            # Парсинг xml-файла
            tree = xml.parse(file)
            # Получение основного тега
            main_tag = tree.getroot()
            # Получение остальных тегов
            tag = main_tag.getchildren()

            # Объявление тегов
            productID = ''
            Year = ''
            Month = ''

            # Перебор элементов основного тега
            for i in tag:
                # Получение дочернего тега
                element = i.getchildren()

                # Перебор элементов дочерних тегов
                for q in element:
                    # Присвоение переменным значения тегов
                    # Если тег = 'productID'
                    if q.tag == "productID":
                        # Получение текста тега
                        productID = q.text
                    # Если тег = 'Year'
                    elif q.tag == "Year":
                        # Получение текста тега
                        Year = q.text
                    # Если тег = 'Month'
                    elif q.tag == "Month":
                        # Получение текста тега
                        Month = q.text

            # Вывод в консоль полученных данных тега Body
            print("Class Pojo [productID = " + productID + ", Year = " + \
                            Year + ", Month = " + Month + "]")
