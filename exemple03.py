# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


while True:
    try:
        n = int(input('Введите число n (один знак)>>>'))
        if 0 < n < 10:
            break
    except ValueError:
        print("Oops! It doesn't look like a number!")

print(
    "n+nn+nnn = ",
    n + (n * 11) + (n * 111))
