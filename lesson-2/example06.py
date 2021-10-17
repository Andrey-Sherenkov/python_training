# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# это словарь? да/ в словаре все через : без = . теперь вроде как надо все переменные вытащить в input
uid = 0
cort_product = []
cort_dict = []
while True:
    name_product = input("введите наименование товара >>")
    product_price = input("введите стоимость товара >>")
    quantity_product = input("введите количество товара >>")
    units_of_measur = input("введите единицы измерения >>")
    uid = uid + 1
    product_dict = {'название': name_product, 'цена': product_price, 'количество': quantity_product,
                    'eд': units_of_measur}
    # print(product_dict)
    cort_dict.append(product_dict)
    product_properties = (uid, product_dict)
    cort_product.append(product_properties)  # собрать кортежи в один список
    inp = input("если завершили ввод введите 1")
    if inp == '1':
        break
print("ch", cort_product)
# # example
# # печать списка
# print("ch", cort_product)
# # заголовки таблицы
# for el in cort_product[0][1].keys():
#     print('tb', el)
# # вызвать количество строк
# print('co', len(cort_product))
# # печать ячейки
# print(cort_product[0][1].get('eд'))
# print('bye', cort_product[0][1]['цена'])
# # /example
new_dict = {}

for el in cort_product[0][1].keys():
    new_list = []
    for ns in range(len(cort_product)):
        new_list.append(cort_product[ns][1].get(el))
    print('raw', el, new_list)
    axe_tmp = {el: set(new_list)}
    print('a', axe_tmp)
    new_dict.update(axe_tmp)
    # new_dict.update(el = list(new_list)) # читается key='el' value=new_list
print('nd', new_dict)
