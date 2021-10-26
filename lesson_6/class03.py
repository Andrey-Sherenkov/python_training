# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name: str
    surname: str
    position: str
    _wage: float
    _bonus: float

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position)
        self._wage = wage
        self._bonus = bonus

    def get_full_name(self):
        full_name = self.name + " " + self.surname
        print(full_name)

    def get_total_income(self):
        total_income = self._wage + self._bonus
        print(f"income {total_income}")


dict_income = {'wage': 100, 'bonus': 1000}
info_work = Position("Alex", "Fox", "Manager", **dict_income)

info_work.get_full_name()
info_work.get_total_income()
