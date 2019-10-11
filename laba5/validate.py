from lxml import etree
from io import StringIO


class Valid:
    def xmlCorrect(self, doc, path_file_xml):
        try:
            # Загрузка XML файла
            with open(path_file_xml, 'r') as xml_file:
                xml_to_check = xml_file.read()
            # Проверка на правильность оформления XML-файла
            doc = etree.parse(StringIO(xml_to_check))
            print('\nXML well formed, syntax ok.')

        # Ошибка файла
        except IOError:
            print('\nInvalid File')

        # Ошибка синтаксиса XML
        except etree.XMLSyntaxError as err:
            print('\nXML Syntax Error')
            exit()
        # Другого вида ошибки
        except:
            print('\nUnknown error, exiting.')
            exit()
        return doc

    def xsdValid(self, doc, path_file_xsd):
        # Валидация XML по XSD
        try:
            # Загрузка XSD файла
            with open(path_file_xsd, 'r') as schema_file:
                schema_to_check = schema_file.read()
            xmlschema_doc = etree.parse(StringIO(schema_to_check))
            xmlschema = etree.XMLSchema(xmlschema_doc)
            xmlschema.assertValid(doc)
            print('\nXML valid, schema validation ok.')
            return True

        except etree.DocumentInvalid as err:
            print('\nSchema validation error')
            exit()

        except:
            print('\nUnknown error, exiting.')
            exit()
