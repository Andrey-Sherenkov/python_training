# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


from datetime import date


class Data:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def type(data: str):
        try:
            dat_digit = [int(x) for x in data.replace("-", " ").split() if x.isdigit()]
            return dat_digit
        except ValueError:
            return 'Указана неправильная дата!'

    @classmethod
    def valid(cls, data):
        try:
            day, moint, yer = Data.type(data)
            if day <= 0 or day > 31:
                return "день введен некорректно"
            elif moint <= 0 or moint > 12:
                return "месяц введен некорректно"
            elif yer <= 1800 or yer > 2999:
                return "год введен некорректно"
            return f'{day:>02}, {moint:>02}, {yer}'
        except ValueError:
            return "Указана неправильная дата!"


print(Data.valid("1-12-1986"))
