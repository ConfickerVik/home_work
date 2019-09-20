import re
import string


class Search:
    def sequence(self, word_list):
        lot_counter = []
        counter = 0
        for word in word_list:
            if word.isdigit():
                counter += 1
            else:
                lot_counter.append(counter)
                counter = 0

        max_counter = lot_counter[0]
        for number in lot_counter:
            if number > max_counter:
                max_counter = number

        print("Наибольшее число цифр, идущих подряд = ", max_counter)


if __name__ == '__main__':
    path = input("Укажите путь до файла с текстом: ")
    try:
        with open(path, "r") as text_file:
            text = text_file.read()
            print("\nФайл успешно принят!")
    except FileNotFoundError:
        print("\nОшибка чтения файла! Файл повреждён, либо не существует")
        exit(0)

    word_list = re.sub('['+string.punctuation+'\n]', ' ', text).split()

    obj = Search()
    obj.sequence(word_list)
