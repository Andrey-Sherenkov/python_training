# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

count = 0

try:
    with open("for_2_ex") as my_obj:
        for line in my_obj:
            count += 1
            print(f"строка {count}  слов {len(line.split())}")  # Ok количество слов, без влияния лишних пробелов

        print("всего строк", count)
except IOError:
    print("Произошла ошибка ввода-вывода!")


# with open('task2.txt', 'r') as file:
#     print(f'Всего строк - {len(file.readlines())}')
#     file.seek(0)
#     for i, l in enumerate(file, 1):
#         print(f'{i} строка - {len(l.split())} слова')