# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
# и строк и сохраните в переменные, выведите на экран.

a = 10
b = 20
print(a - b)

name = input("Введите имя >>>")
while True:
    try:
        age = int(input('Введите возраст >>>'))
        break
    except ValueError:
        print("Oops! It doesn't look like a number!")
print("Меня зовут", name, "мне", age, "лет")
