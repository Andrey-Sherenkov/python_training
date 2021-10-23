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



# profit = {}
# pr = {}
# prof = 0
# prof_aver = 0
# i = 0
# with open('l5.7_text.txt', 'r') as file:
#     for line in file:
#         name, firm, earning, damage = line.split()
#         profit[name] = int(earning) - int(damage)
#         if profit.setdefault(name) >= 0:
#             prof = prof + profit.setdefault(name)
#             i += 1
#     if i != 0:
#         prof_aver = prof / i
#         print(f'Прибыль средняя - {prof_aver:.2f}')
#     else:
#         print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
#     pr = {'средняя прибыль': round(prof_aver)}
#     profit.update(pr)
#     print(f'Прибыль каждой компании - {profit}')
#
# with open('l5.7_json.json', 'w') as write_js:
#     json.dump(profit, write_js)
#
#     js_str = json.dumps(profit)
#     print(f'Создан файл с расширением json со следующим содержимым: \n '
#           f' {js_str}')



# with open('task7.txt', 'r', encoding='utf-8') as file:
#     firms = {}
#     total = []
#     for line in file.readlines():
#         firm, _, proceeds, costs = line.split()
#         profit = float(proceeds) - float(costs)
#         if profit > 0:
#             total.append(profit)
#         firms.update({firm: profit})
#     avg_profit = round(sum(total) / len(total), 2)
#     result = [firms, {'average profit': avg_profit}]
#     with open('result.json', 'w', encoding='utf-8') as file_json:
#         json.dump(result, file_json)
