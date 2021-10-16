# 4 Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

open_data = [1.414, -2]


def my_func_recurs(x, y):
    """
    рекурсивная функция возводит число в степень
    :param x: основание
    :param y: степень
    :return: результат возведения числа в степень
    """
    if y > 1:
        return (x * my_func_recurs(x, y - 1))
    if y < -1:
        return (1 / my_func_recurs(x, - y))  # угадай почему так
    return x


def my_func_1(x, y):
    a = 1
    for el in range(abs(y)):
        a = a * x
    if y < 0:
        return (1 / a)
    else:
        return a


# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
def my_func_no(x, y):
    res = x ** y
    return res


print("f1 ", my_func_recurs(*open_data))
print("f2 ", my_func_1(*open_data))
print("f3 ", my_func_no(*open_data))
