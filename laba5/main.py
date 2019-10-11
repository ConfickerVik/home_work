from laba5.functions.validate import Valid
from laba5.parsers.DOM import DOMParser
from laba5.parsers.SAX import SAXParser
from laba5.functions.XSL import XSLhtml

while True:
    path_file_xml = input("\nВведите путь до XML-файла: ")
    path_file_xsd = input("\nВведите путь до XSD-файла: ")
    path_file_xsl = input("\nВведите путь до XSL-файла: ")

    doc = ''
    validate = Valid()
    doc = validate.xmlCorrect(doc, path_file_xml)
    resultValid = validate.xsdValid(doc, path_file_xsd)

    xsl = XSLhtml()
    xsl.translate(path_file_xml, path_file_xsl)

    if resultValid is True:
        print("\nРеализованные парсеры:\n"
              "1. DOM \n"
              "2. SAX \n")
        num = input("Выберите парсер, который хотите применить: ")
        if num == '1':
            print("\nРезультат работы парсера DOM:\n")
            parse = DOMParser()
            parse.startDom(path_file_xml)
        elif num == '2':
            print("\nРезультат работы парсера SAX:\n")
            parse = SAXParser()
            parse.startSax(path_file_xml)
        else:
            print("\nНеправильнный ввод! Программа закрывается!")
            exit()

    retry = input("\nХотите проверить новый XML-файл? (y/n): ")
    if retry == "y":
        continue
    elif retry == "n":
        print("\nСпасибо, что пользовались моей программой) Всего доброго XD")
        exit()
    else:
        print("\nНеправильный ввод! Программа закрывается!")
        exit()
