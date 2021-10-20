# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
#
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
import my_library


while True:
    try:
        n = int(input("введите целое число n >>"))
        break
    except ValueError:
        print("это не число")

# def fact(x):
#     for el in [x for x in range(1, x + 1)]:
#         yield el


a = 1
for el in my_library.fact(n):
    a = a * el

print('n! = ', a)

#


def fact(n):
    res = 1
    for el in range(1, n + 1):
        res *= el
        yield res


for el in fact(4):
    print(el)