import re
import string


class Search:
    def compare(self, word_list):
        print("\nСлова удовлетворяющие условию задачи: ")
        for count in range(len(word_list) - 1):
            word = (word_list[count][-1]).lower()
            next_word = (word_list[count + 1][0]).lower()
            if word == next_word and word.isalpha() and next_word.isalpha():
                print(word_list[count], " и ", word_list[count + 1])


if __name__ == '__main__':
    path = input("Укажите путь до файла с текстом:")
    try:
        with open(path, "r") as text_file:
            text = text_file.read()
            print("\nФайл успешно принят!")
    except FileNotFoundError:
        print("\nОшибка чтения файла! Файл повреждён, либо не существует")
        exit(0)

    word_list = re.sub('['+string.punctuation+'\n]', ' ', text).split()

    obj = Search()
    obj.compare(word_list)
