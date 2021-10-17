# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


my_numbers = [7, 2, 1]


# честное решение.
def my_func(my_list_in):
    my_list = my_list_in.copy()  # копирование чтобы не менять входной лист
    max1 = min(my_list)  # min потому что влом искать минимально возможную константу -inf+1
    for el in range(len(my_list)):
        if my_list[el] > max1:
            max1 = my_list[el]
            my_list[el] = min(my_list)
            #print("max1", max1)
            #print("list", my_list)
            break
    max2 = min(my_list)
    for el in range(len(my_list)):
        if my_list[el] > max2:
            max2 = my_list[el]
            my_list[el] = min(my_list)
            #print("max2", max2)
            #print("list", my_list)
            break
    return max1 + max2


# решение прибитое гвоздяти к трём элементам, зато краткое
def my_func_min(in_list):
    abc = in_list.copy()
    #print(abc)
    return sum(abc) - min(abc)


# решение с юмором
def my_func_sort(my_list_in):
    """
    сортирует список и суммирует два последних элемента
    :param my_list:
    :return:
    """
    #print(my_list)
    my_list = my_list_in.copy()
    my_list.sort()
    #print(my_list)
    #print(int(my_list[len(my_list) - 1]))
    #print(int(my_list[len(my_list) - 2]))
    return int(my_list[len(my_list) - 1]) + int(my_list[len(my_list) - 2])


print(my_func(my_numbers))
print(my_func_min(my_numbers))
print(my_func_sort(my_numbers))