# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
while True:
    try:
        number = int(input('Введите целое положительное число: '))
        if number > 0:
            break
    except ValueError:
        print("Oops! It doesn't look like a number!")

max_num = 0

while number > 0:
    if (number % 10) > max_num:
        max_num = number % 10
    number = number // 10
print("наибольшее число:", max_num)
