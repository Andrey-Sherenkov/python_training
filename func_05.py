# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.


var_sum = 0
cont_my_na = True


def parser_sum(user_string):
    """
    возвращает сумму чисел
    :param user_string:строка с числами
    :return: сумма, либо cont_my_na = False
    """
    temp = 0
    user_list = user_string.split(' ')
    #print(user_list)
    for el in range(len(user_list)):
        if user_list[el].isdigit():
            temp += float(user_list[el])
        else:
            global cont_my_na
            cont_my_na = False
            break
    #print(temp)
    return temp


print("Введите  числа через пробел, сумирование будет продолжаться пока не появится не число ")
while cont_my_na:
    var_sum += parser_sum(input(">>>"))
    print(var_sum)
print("goodbay")