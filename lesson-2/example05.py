# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
my_list.sort()
my_list.reverse()
while True:
    try:
        rating_user = int(input('введите целое число>>>'))
        break
    except ValueError:
        print("это не число")

for el in range(len(my_list)):
    if my_list[el] < rating_user:
        my_list.insert(el, rating_user)
        print(my_list)
        exit(0)  # выход после вставки елемента

my_list.insert(len(my_list), rating_user)  # добавить в конец списка если не нашли соседа
print(my_list)

# здесь жестко оптимизированная версия и не выполняет условия задачи полностью
# my_list = [7, 5, 3, 3, 2]
# while True:
#     try:
#         rating_user = int(input('введите целое число 0т 1 до 10>>>'))
#         if 0 < rating_user <= 10:
#             my_list.append(rating_user)
#             my_list.sort()
#             print(my_list, "для выхода нажмите не число")
#     except ValueError:
#         break
