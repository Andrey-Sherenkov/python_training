# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
#
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length: int
    _width: int
    _mass_quad: int = 25
    _thickness: int = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        mass = self._length * self._width * self._mass_quad * self._thickness / 1000
        print(
            f"расчетная масса покрытия шириной {self._length} м, длинной {self._width} м, толщиной {self._thickness} см = {mass} Т")


new_road = Road(20, 5000)
new_road.calc()