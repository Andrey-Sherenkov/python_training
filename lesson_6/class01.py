# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

# теперь есть время и делай  - выбирай. sleep(7) - задержка 7 секунд перед следующей операцией
# если задежки внутри класса надо городить отдельный поток и команду стоп
# логика работы светофора целиком внутри класса

# или клас переключает цвета, а все вызовы времени снаружи
# из текста задачи непонятно как делать, думай, нужные кусочки уже есть для всего, потоки можно глянуть в коде для осцилографа

# так то логично, если я обращаюсь к методу и передаю задержки - и потом все работает без дополнительных вызовов, но как сделать стоп?
# стоп дополнительная функция о которой не слова и с ней связанны потоки
# в методичке есть потоки? thread? - нет значит подругому?
# по другому это значит вне класса? все слееп и тиме вне класса.
# в метод отдаёшь желаемый цвет и ждёшь до следующего переключения, потом снова метод с слндующим цветом, будет похоже на Г


import time


class TrafficLight:
    __color: str = "зеленый"  # Атрибут реализовать как приватный.

    def running(self, color):
        if color == "красный":
            if self.__color == "зеленый":
                self.__color = "красный"
                print(f"{self.__color} \ttime: {time.time()}")
            else:
                print(f"{self.__color}  {color} ,нарушен порядок")
        elif color == "желтый":
            if self.__color == "красный":
                self.__color = "желтый"
                print(f"{self.__color} \t\ttime: {time.time()}")
            else:
                print(f"{self.__color}  {color} ,нарушен порядок")
        elif color == "зеленый":
            if self.__color == "желтый":
                self.__color = "зеленый"
                print(f"{self.__color} \ttime: {time.time()}")
            else:
                print(f"{self.__color}  {color} ,нарушен порядок")
        else:
            print(f"not valid color:  \"{color}\"  use: красный, желтый, зеленый")


TL = TrafficLight()

print("run")
TL.running("красный")
time.sleep(7)
TL.running("желтый")
time.sleep(2)
TL.running("зеленый")
time.sleep(2)
print("test")
TL.running("gt")
TL.running("зеленый")
TL.running("желтый")
TL.running("красный")
TL.running("зеленый")

print("stop")


# class TrafficLight:
#     __color: str = "зеленый"  # Атрибут реализовать как приватный.
#
#     def running(self):
#         self.__color = "красный"
#         print(self.__color)
#         time.sleep(7)
#         self.__color = "желтый"
#         print(self.__color)
#         time.sleep(2)
#         self.__color = "зеленый"
#         print(self.__color)
#         # это куски для отладки, а не рабочий код!
#         # print("run")
#         # print(self.__color)    # Ok
#         # print(time.time())     #  1635063510.8590522
#         # print(time.ctime())
#         # print("sleep 7")
#         # time.sleep(7)           # Ok
#         # print("stop")
#
#
# TL = TrafficLight()
#
# print("run")
# TL.running()
# print("stop")
#
# #print(TL._TrafficLight__color)  # error, нет доступа к приватным_ это не должно работать!!!
#
#
# # только вместо принта вызов класса, выглядит странно
# # for _ in range(2):
# #     print("красный")
# #     time.sleep(7)
# #     print("желтый")
# #     time.sleep(2)
# #     print("зеленый")
# #     #time.sleep(7)
# #     if input() == "s":
# #         break
