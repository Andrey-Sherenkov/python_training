# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def f_def_named(ai, ab):
    if ab != 0:
        def_val = ai / ab
        return def_val
    else:
        return "деление на ноль"


def f_def(*pos):
    if pos != None and len(pos) > 1:
        if pos[1] != 0:
            def_val = pos[0] / pos[1]
            return def_val
        else:
            return None


while True:
    try:
        r_val = float(input("Укажите переменную: "))
        h_val = float(input("Укажите переменную: "))
        break
    except ValueError:
        print('попробуй еще')

print(f_def(r_val, h_val))
