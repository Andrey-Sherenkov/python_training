# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

while True:
    try:
        mount = int(input('введите целое число 0т 1 до 12 >>>'))
        if 0 < mount <= 12:
            break
    except ValueError:
        print("поробуйте еще раз")
season_list: list = ['зима', 'весна', 'лето', 'осень']
season_dict: dict = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень'}
ind_val = mount
if ind_val > 11:
    ind_val = 0
ind_val = ind_val // 3
print(season_dict.get(ind_val))
print(season_list[ind_val])
