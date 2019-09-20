import re
import string


class Search:
    def search_sample(self, word_list, word_sample):
        for word in word_list:
            if word.lower() == word_sample.lower():
                with open("result2_4.txt", "w") as file:
                    file.write(word)
                print("")


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

    word_sample = input("Введите слово для поиска: ")

    obj = Search()
    obj.search_sample(word_list, word_sample)
