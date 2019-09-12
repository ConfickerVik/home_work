import sys


class Result:
    def sum(self, arg1, arg2):
        total_sum = arg1 + arg2
        return total_sum

    def multiply(self, arg1, arg2):
        total_mul = arg1 * arg2
        return total_mul


if __name__ == "__main__":
    argument_1 = int(sys.argv[1])
    argument_2 = int(sys.argv[2])
    obj = Result()
    result_sum = obj.sum(argument_1, argument_2)
    result_mul = obj.multiply(argument_1, argument_2)
    print("Сумма двух целочисленных аргументов равна: ", result_sum,
          "\nПроизведение двух целочисленных аргуметов равна: " ,result_mul)
    
