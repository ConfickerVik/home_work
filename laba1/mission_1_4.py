import sys


class Result_sum:
    def sum(self, total_sum, arg):
        total_sum += arg
        return total_sum


class Result_mul:
    def multiply(self, total_mul, arg):
        total_mul *= arg
        return total_mul


if __name__ == "__main__":
    argv = sys.argv
    obj_sum = Result_sum()
    obj_mul = Result_mul()
    result_sum = 0
    result_mul = 1
    try:
        for argument in range(1, len(argv)):
            result_sum = obj_sum.sum(result_sum, int(argv[argument]))
            result_mul = obj_mul.multiply(result_mul, int(argv[argument]))
        print("Сумма целочисленных аргументов равна: ", result_sum,
              "\nПроизведение целочисленных аргуметов равна: " ,result_mul)
    except ValueError:
        print("Неверно введены данные!")
