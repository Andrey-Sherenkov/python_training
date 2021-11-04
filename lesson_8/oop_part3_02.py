# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Calc():
    def __init__(self, number: int):
        self.number = number

    def __truediv__(self, other):
        try:
            if other.number != 0:
                return Calc(round(self.number / other.number))
            else:
                raise OwnError("На ноль делить не буду")
        except OwnError as err:
            print("Делить на ноль нельзя!")

    def __str__(self):
        return f"результат деления {self.number}"


num_1 = int(input('Введите делимое: '))
num_2 = int(input('Введите делитель: '))

a = Calc(num_1)
b = Calc(num_2)

print(a / b)
