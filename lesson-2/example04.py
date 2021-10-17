# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове

user_string = input("Введите строку из нескольких слов>>>")
user_list = user_string.split(' ')  # input всегда строка для преобразования в list нужен split

for el in range(len(user_list)):
    print(el + 1, " ", "{:.10}.".format(user_list[el]))

# другое решение
for ind, el1 in enumerate(user_list, 1):
    print(ind, "{:.10}.".format(el1))
