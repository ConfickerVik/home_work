from tkinter.filedialog import askopenfilename
from Create_xml import CreateXml
import sys


open_file = askopenfilename(filetypes=[('Txt files', '.txt')])  # Выбор текстового файла
file = open(open_file, 'r')  # Открытие для чтения
read_file = file.readline()  # Считывание файла
read_f = read_file.split()
c = 0
f = 3
mas = []

if read_file == "":
    print("\nФайл пуст!")
    sys.exit()
else:
    for i in read_f:
        if i == ",":
            c += 1

    for j in range(c+1):
        mas.append(read_f[f])
        f += 4

    CX = CreateXml()
    CX.create_xml(mas)
    print("Успешно!")
