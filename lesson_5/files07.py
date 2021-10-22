# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

try:
    with open("for_ex07") as my_obj:
        my_dict_profit = {}
        my_dict_avg_profit = {}

        count = 0
        sum_profit = 0  # переменная для суммирования
        for lines in my_obj:  # работа со строками
            profit: int = 0
            num = [int(x) for x in lines.split() if x.isdigit()]  # для распознания цифр в строке
            for line in num:
                profit = num[0] - num[1]
            if profit >= 0:
                count += 1
                sum_profit += profit
            avg_profit = sum_profit / count
            content = lines.split()
            my_dict_avg_profit["average_profit"] = avg_profit
            my_dict_profit[content[0]] = profit  # заносим в словарь то, что требуется
        my_list = [my_dict_profit, my_dict_avg_profit]
        print(my_list)

        with open("my_file.json", "w") as write_f:  # запись в json файл
            json.dump(my_list, write_f)
except IOError:
    print("Произошла ошибка ввода-вывода!")
