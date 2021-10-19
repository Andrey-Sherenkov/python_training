# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys
from lesson_4 import my_library


file, work_hours, rate_hours, prize = sys.argv

print(my_library.calculate_zp(int(work_hours), int(rate_hours), int(prize)))

