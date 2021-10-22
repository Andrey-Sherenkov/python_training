# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
#
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


try:

    with open("for_ex03") as my_obj:
        sum_solari = 0
        count = 0
        poor_list = []
        for line in my_obj:
            content = line.split()  # создается список из элементов строки
            sum_solari += (float(content[1]))  # элемент с порядковым номером 1 переводим в флоату
            count += 1
            if (float(content[1])) < 20000:
                # print(content[0], content[1])
                poor_list.append(content[0])
        print(f"сотрудники с зп меньше 20000 :{poor_list}")
        avg_solari = sum_solari / count
        print(f"средняя ЗП =  {avg_solari:,.2f}")
except IOError:
    print("Произошла ошибка ввода-вывода!")