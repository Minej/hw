from math import sqrt, log, e


def enter_num():
    a = float(input("Введите число a: "))
    x = float(input("Введите число х: "))
    t = float(input("Введите число t: "))

    return calc(a, x, t)


def calc(a, x, t):
    y_end = 0.9
    y_step = 0.2
    y = 0.3

    while y < y_end:
        y_float = float(y)
        z = round((a ** 3 * sqrt(x + log(y_float, e) ** 2)) / abs(t ** 3), 2)
        print(f"z = {z} при y = {y}")
        y += y_step

    return True


enter_num()
