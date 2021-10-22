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
