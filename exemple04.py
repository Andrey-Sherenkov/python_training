# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))
max_num = 0

if number < 0:
    print("надо целое положительное число")
    exit(1)
while number > 0:
    print(number % 10)
    if (number % 10) > max_num:
        max_num = number % 10
    number = number // 10
print("наибольшее число:", max_num)
