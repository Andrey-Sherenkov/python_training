# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce


def my_func(prev_el, el):
    # prev_el - предыдущий элемент, первый как есть, 2-ой и далее приходит через return el
    # el - текущий элемент, перебор элементов с второго
    # print(f"mfi {prev_el}   {el}")
    return prev_el * el


my_list = [x for x in range(100, 1001, 2)]
print(my_list)

number = (reduce(my_func, my_list))
print(number)

#
def mult_even_num_func(range_start, range_stop):
    num_list = [el for el in range(range_start, range_stop + 1) if el % 2 == 0]
    return reduce(lambda a, b: a * b, num_list)


print(mult_even_num_func(100, 1000))
