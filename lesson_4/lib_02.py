# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from functools import reduce
from random import randint


def my_func(prev_el, el):
    # prev_el - предыдущий элемент, первый как есть, 2-ой и далее приходит через return el
    # el - текущий элемент, перебор элементов с второго
    # print(f"mfi {prev_el}   {el}")
    if el > prev_el:
        var_list.append(el)
    return el


var_list = []
my_list = [randint(0, 1000) for x in range(10)]

print("список", my_list)
reduce(my_func, my_list)
print("результат", var_list)


# Другой вариант

def get_right_max_list_func(src_list):
    return [el for el in src_list[1:] if el > src_list[src_list.index(el) - 1]]


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
max_list = get_right_max_list_func(my_list)
print(my_list)
print(max_list)