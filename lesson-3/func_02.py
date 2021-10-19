# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

my_list = ["иван",  "иванов", "1999", "omsk", "iii@mail.ru", 899999]


def my_func(first_name, last_name, year_of_birth, citi, email, phone):
    print(
        f"first_name - {first_name} last_name - {last_name} year_of_birth {year_of_birth} citi-{citi} email {email}  phone:{phone}")
    return 0


my_func(*my_list)
my_func(first_name="иван", last_name="иванов", year_of_birth="1999", citi="omsk", email="iii@mail.ru", phone=899999)
