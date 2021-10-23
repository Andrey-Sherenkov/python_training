# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
# твой косяк? мой
try:
    with open("for_ex05", "w+") as my_obj:
        sum_number: float = 0
        my_sting = input("новая строка >>")
        my_obj.write(my_sting)  # пишем строку чисел в файл
        my_obj.seek(0)  # курсор в начало
        content = my_obj.read()  # читаем из фала
        cont_list = content.split()  # создаем список
        for line in cont_list:
            sum_number += (float(line))  # переводим элементы списка в флоату и суммируем
        print(f"сумма чисел = {sum_number}")
        print(sum(map(float, cont_list)))
except IOError:
    print("Произошла ошибка ввода-вывода!")
except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')

# with open('task5.txt', 'w+', encoding='utf-8') as file:
#     file.write(input('Введите набор чисел, разделенных пробелом: '))
#     file.seek(0)
#     print(sum([int(i) for i in file.readline().split()]))