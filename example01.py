# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list_of_values = [1, 2, 2.1, 'text', None]
print(list_of_values)

for value in list_of_values:
    print(value, type(value))