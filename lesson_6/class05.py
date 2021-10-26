# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title: str

    def __init__(self, title="red"):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        super().draw()
        print("Рисуем ручкой", self.title)


class Pencil(Stationery):

    def draw(self):
        super().draw()
        print("Рисуем карандашом", self.title)


class Handle(Stationery):

    def draw(self):
        super().draw()
        print("Рисуем маркером", self.title)


paint1 = Stationery()
paint2 = Pen("blue")
paint3 = Pencil()
paint4 = Handle()

paint1.draw()
print("-------------------")
paint2.draw()
print("-------------------")
paint3.draw()
print("-------------------")
paint4.draw()
