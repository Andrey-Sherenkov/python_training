# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
#
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
import random


def unique_list(src_list):
    return [el for el in src_list if src_list.count(el) == 1]


my_list = [random.randint(10, 100) for x in range(0, 10)]
sampling = random.choices(my_list, k=10)
print(my_list)
print("Выборка с методом choices ", sampling)
print("Выборка без повторов ", unique_list(sampling))

