# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
# любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум
# возможностей, изученных на уроках по ООП.


class LimitExceeded(Exception):
    def __init__(self, message):
        self.message = message


class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment, quantity: int):
        """ Метод для добавления в словарь экземпляров оборудования в соответствии с group_name() выбранного класса
        если оборудование уже имеется в словаре добавится количество quantity
        """
        try:
            self._dict.setdefault(equipment.group_name(), {})
            if self._dict[equipment.group_name()].get(str(equipment)) is None:  # проверка отсутствия товара в списке
                self._dict.setdefault(equipment.group_name(), {}).update({str(equipment): int(quantity)})
            else:  # суммируем количество
                self._dict.setdefault(equipment.group_name(), {}).update(
                    {str(equipment): self._dict[equipment.group_name()].get(str(equipment)) + int(quantity)})
        except TypeError:
            print("ошибка ввода параметров")
        except ValueError:
            print("ошибка типа параметров")

    def extract(self, equipment, quantity: int):
        """
        метод для уменьшения количества единиц оборудования. Если введенное количество {quantity} равно наличному
        количеству - удаляем это оборудование из словаря
        :param equipment:
        :param quantity: количество
        :return:
        """
        try:
            if self._dict[equipment.group_name()][str(equipment)] > int(quantity):
                self._dict[equipment.group_name()][str(equipment)] -= int(quantity)
            elif self._dict[equipment.group_name()][str(equipment)] == int(quantity):
                del self._dict[equipment.group_name()][str(equipment)]
            else:
                raise LimitExceeded(f"введенное количество превышает наличное")
        except TypeError:
            print("ошибка типа параметров")

        except KeyError:
            print("ошибка ввода параметров")
        except LimitExceeded:
            print(
                f"введенное количество {quantity} превышает наличное "
                f"{self._dict[equipment.group_name()][str(equipment)]}")

    def revise(self):
        """ Ревизия склада"""
        print(f"сейчас на складе: {self._dict}")


class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.make} {self.year}'


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.make} {self.year}'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)


class Departament(Sklad):

    def __init__(self):
        super().__init__()
        print("вызов конструктора класса наследника")
        self._dict = {}

    def revise(self):
        print(f"сейчас в подразделении емеется: {self._dict}")


warehaus = Sklad()
warehaus.revise()
# создаем объект и добавляем
product1 = Scaner('hp', '321', 90)
warehaus.add_to(product1, 5)
warehaus.revise()
product1 = Scaner('hp', '321', 90)
warehaus.add_to(product1, 9)
warehaus.revise()
product1 = Scaner('hp', '311', 97)
warehaus.add_to(product1, 45)
warehaus.revise()
product1 = Scaner('hp', '330', 99)
warehaus.add_to(product1, 8)
warehaus.revise()
product1 = Printer('e-320', 'sony', 126, 2018)
warehaus.add_to(product1, 1)

# # ревизия склада
warehaus.revise()
# # забираем со склада и ревизия склада
product1 = Scaner('hp', '321', 90)
warehaus.extract(product1, 8)
warehaus.revise()

# # проверка на ошибки

print("проверка на ошибки")
# ошибка типа параметров
product1 = Scaner('hp', '311', 97)
warehaus.add_to(product1, "ii")
# превышение наличного количества
product1 = Scaner('hp', '321', 90)
warehaus.extract(product1, 66)
warehaus.revise()
print("добавить сканер")  # Ok
product1 = Scaner('xz', '311', 97)
warehaus.add_to(product1, 100)
warehaus.revise()
# ошибка ввода параметров
product1 = Scaner('hp', "311", "90")
warehaus.extract(product1, 8)
warehaus.revise()

# передачу в определенное подразделение компании.
d = Departament()
d.revise()
product1 = Scaner('xz', '311', 97)
d.add_to(product1, 1)
d.revise()
warehaus.extract(product1, 1)
warehaus.revise()
