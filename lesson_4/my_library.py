# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.

def calculate_zp(work_hours, rate_hours, prize):
    # print("lw", work_hours ,"r",rate_hours, "p", prize)
    total = (work_hours * rate_hours) + prize
    return total


def sci_notation(number, sig_fig=8):
    ret_string = "{0:.{1:d}e}".format(number, sig_fig)
    a, b = ret_string.split("e")
    b = int(b)  # removed leading "+" and strips leading zeros too.
    return a + " * 10^" + str(b)
# максимум 10^308


def fact(x):
    for el in [x for x in range(1, x + 1)]:
        yield el