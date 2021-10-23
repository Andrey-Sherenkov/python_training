# Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4

# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


try:
    new_obj_new = open("for_ex04_new", "w")
    my_obj = open("for_ex04")
    for line in my_obj:
        # print(line.replace("One", "Один").replace("Two", "Два").replace("Three", "Три").replace("Four", "Четыре"))
        new_obj_new.write(
            line.replace("One", "Один").replace("Two", "Два").replace("Three", "Три").replace("Four", "Четыре"))
    my_obj.close()
    new_obj_new.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    my_obj.close()
    new_obj_new.close()


# numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
#
# with open('task4.txt', 'r', encoding='utf-8') as file, \
#      open('result.txt', 'w', encoding='utf-8') as output:
#     i = 0
#     for line in file.readlines():
#         i += 1
#         number = line.split()[0]
#         output.write(f'{numbers[number]} - {i}\n')