# 4.Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed: int = 0
    color: str
    name: str
    is_police: bool
    direction: int = 0  # положение руля. -360: левый поворот, +360: правый поворот

    def __init__(self, speed, color, name, direction=0):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = direction

    def name_car(self):
        print(self.color, self.name)

    def go(self):
        if self.speed > 0:
            print("машина поехала")

    def stop(self):
        if self.speed == 0:
            print("машина остановилась")

    def turn(self):
        if self.direction > 0 and self.speed > 0:
            print(f"правый поворот {self.direction}")
        elif self.direction and self.speed > 0:
            print(f"левый поворот {self.direction}")
        else:
            pass

    def show_speed(self):
        if self.speed < 0:
            print("скорость не может отрицательной")
        elif self.speed == 0:
            pass
        else:
            print(f"текущая скорость {self.speed}")


class TownCar(Car):

    def __init__(self, speed, color, name, direction=0):
        super().__init__(speed, color, name, direction)

    def name_car(self):
        print(self.color, self.name)

    def go(self):
        super().go()

    def stop(self):
        super().stop()

    def turn(self):
        super().turn()

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("сообщение о превышении скорости")


class SportCar(Car):
    def __init__(self, speed, color, name, direction=0):
        super().__init__(speed, color, name, direction)

    def name_car(self):
        print(self.color, self.name)

    def go(self):
        super().go()

    def stop(self):
        super().stop()

    def turn(self):
        super().turn()

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("сообщение о превышении скорости")


class WorkCar(Car):
    def __init__(self, speed, color, name, direction=0):
        super().__init__(speed, color, name, direction)

    def name_car(self):
        print(self.color, self.name)

    def go(self):
        super().go()

    def stop(self):
        super().stop()

    def turn(self):
        super().turn()

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("сообщение о превышении скорости")


class PoliceCar(Car):
    def __init__(self, speed, color, name, direction=0, is_police: bool = True):
        super().__init__(speed, color, name, direction)
        self.is_police = is_police

    def name_car(self):
        if self.is_police:
            print(self.color, self.name, "полиция")
        else:
            print(self.color, self.name)

    def go(self):
        super().go()

    def stop(self):
        super().stop()

    def turn(self):
        super().turn()

    def show_speed(self):
        super().show_speed()
        if self.speed > 60 and self.is_police == False:
            print("сообщение о превышении скорости")


car1 = Car(0, "red", "kalina", -80)
car1.name_car()
car1.go()
car1.show_speed()
car1.turn()
car1.stop()

print("----------------------")
car2 = TownCar(70, "blue", "BMV", 70)
car2.name_car()
car2.go()
car2.show_speed()
car2.turn()
car2.stop()

print("----------------------")
car3 = WorkCar(50, "black", "Volvo", 25)
car3.name_car()
car3.go()
car3.show_speed()
car3.turn()
car3.stop()

print("----------------------")
car4 = PoliceCar(70, "black", "Volvo", 25, False)
car4.name_car()
car4.go()
car4.show_speed()
car4.turn()
car4.stop()
