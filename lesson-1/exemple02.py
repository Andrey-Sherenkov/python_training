# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
while True:
    try:
        time_sec = int(input('Введите число секунд >>>'))
        break
    except ValueError:
        print("Oops! It doesn't look like a number!")


seconds = time_sec % 60
minutes = (time_sec // 60) % 60
hours = (time_sec // 60) // 60
print(f"{hours}:{minutes}:{seconds}")
print(f'{hours:>02}:{minutes:>02}:{seconds:>02}')
