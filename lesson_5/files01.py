# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
#

import os

with open("file.txt", "w+") as f_obj:
    while True:
        my_sting = input("новая строка >>")
        if my_sting == '':
            break
        # print(my_sting, file=f_obj)   # запись строки в файл с переносом строки
        f_obj.write(my_sting + "\n")  # запись строки в файл с переносом строки

    f_obj.seek(0)
    content = f_obj.read()
    print(content)

# try:
#     with open("text.txt") as my_obj:
#         for line in my_obj:
#             print(line)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")

# with open("python.txt", "w") as f_obj:
#     print("Необычная работа функции print", file=f_obj)

# os.remove('') # удаление файла
