#  Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
#  практических и лабораторных занятий по этому предмету и их количество.
#  Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#  Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
#  Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re

try:
    with open("for_ex06") as my_obj:
        my_dict = {}
        for lines in my_obj:
            sum_number: int = 0  # переменная для суммирования
            # print(lines)
            content = lines.split()
            num = re.findall(r'\d+', lines)  # готовая функция для распознания цифр в строке
            for line in num:
                sum_number += (int(line))  # и суммируем
            my_dict[content[0]] = sum_number  # заносим в словарь то, что требуется
        print('итоговый словарь', my_dict)

except IOError:
    print("Произошла ошибка ввода-вывода!")


# with open('test6.txt', 'r', encoding='utf-8') as read_file:
#     res_dict = {}
#     all_read_lines = read_file.readlines()
#     for line in all_read_lines:
#         if len(line):
#             subject = line.split()
#             hours_sum = 0
#             for hours in subject[1:]:
#                 if len(hours) > 1:
#                     hours_sum += int(hours.split('(')[0])
#             res_dict[subject[0]] = hours_sum
#     print(f"\t{res_dict}\n")


# with open('task6.txt', 'r', encoding='utf-8') as file:
#     result = {}
#     for line in file.readlines():
#         subject, *lessons = line.split()
#         total = sum([int(i.strip('(лабпр)')) for i in lessons if i.strip('(лабпр)').isdigit()])
#         result.update({subject.strip(':'): total})
#     print(result)