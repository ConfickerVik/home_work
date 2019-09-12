import sys


class Check_pass:
    def check(self, line):
        template = "kukus"
        if line == template:
            print("Пароль совпадает!")
        else:
            print("Пароль не совпадает!")


if __name__ == "__main__":
    line = str(sys.argv[1])
    obj = Check_pass()
    obj.check(line)
