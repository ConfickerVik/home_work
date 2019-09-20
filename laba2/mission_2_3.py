import re


class Refactor:
    def refactoring(self, text):
        try:
            word_list = []
            int_elements = []
            for string_element in text:
                list_element_string = re.sub('[\n]', ' ', string_element).split()
                if len(text) == len(list_element_string):
                    for element in list_element_string:
                        int_elements.append(int(element))
                    word_list.append(int_elements)
                    int_elements = []
                else:
                    print("\nМатрица некорректна")
                    exit(0)
            return word_list
        except ValueError:
            print("\nМатрица некорректна")


class Trans:
    def transpose(self, matr):
        res = []
        n = len(matr)
        m = len(matr[0])
        print("\nРазмер матрицы %s на %s" % (n, m))
        for j in range(m):
            tmp = []
            for i in range(n):
                tmp = tmp+[matr[i][j]]
            res = res+[tmp]
        return res


if __name__ == '__main__':
    path = input("Укажите путь до файла с текстом: ")
    try:
        with open(path, "r") as text_file:
            text = text_file.readlines()
            print("\nФайл успешно принят!")
    except FileNotFoundError:
        print("\nОшибка чтения файла! Файл повреждён, либо не существует")
        exit(0)

    obj = Refactor()
    matrix = obj.refactoring(text)

    print("Исходная матрица:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

    obj = Trans()
    trans_matrix = obj.transpose(matrix)

    print("\nТранспонированная матрица:")
    for i in range(len(trans_matrix)):
        for j in range(len(trans_matrix[i])):
            print(trans_matrix[i][j], end=' ')
        print()
