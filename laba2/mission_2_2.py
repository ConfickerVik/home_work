
class Upgrade:
    def replacement(self, path, text, current, substiture):
        if current in text:
            open(path, "w").write(text.replace(current, substiture))
        print("\nЗамена прошла успешно")


if __name__ == '__main__':
    path = input("Укажите путь до файла с текстом:")
    try:
        with open(path, "r") as text_file:
            text = text_file.read()
            print("\nФайл успешно принят!")
    except FileNotFoundError:
        print("\nОшибка чтения файла! Файл повреждён, либо не существует")
        exit(0)

    current_word = 'public'
    substitute_word = 'private'

    obj = Upgrade()
    obj.replacement(path, text, current_word, substitute_word)