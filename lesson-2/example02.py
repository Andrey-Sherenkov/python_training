# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_string = input("Введите список через запятую>>>")
user_list = user_string.split(',')  # input всегда строка для преобразования в list нужен split
user_list2 = user_list.copy()  # list = list - работает как указатель! (для хранения исходного списка)

symbols = user_list
for el in range(len(symbols) // 2):  # количество итераций  = количество элементов //2
    tmp = symbols[el * 2]  # порядковый номер элемента*2, чтобы обеспечить нужный шаг
    symbols[el * 2] = symbols[el * 2 + 1]
    symbols[el * 2 + 1] = tmp
str_arrange = ', '.join(symbols)  # здесь добавлен "," между элементами
print("список", symbols)  # выводим список
print("строка", str_arrange)  # выводим строку

# другой вариант решения
symbols = user_list2
var_len = len(symbols)
if len(symbols) % 2 > 0:  # проверка на четность
    var_len = len(symbols) - 1  # если нечетное -1
for el in range(0, var_len, 2):  # rang от 0 до var_len с шагом 2
    tmp = symbols[el]
    symbols[el] = symbols[el + 1]
    symbols[el + 1] = tmp
str_arrange = ', '.join(symbols)
print(symbols)
print(str_arrange)
