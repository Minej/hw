from math import sqrt


def enter_num() -> float:
    x1 = int(input("Введите точку x1: "))
    x2 = int(input("Введите точку x2: "))
    x3 = int(input("Введите точку x3: "))
    y1 = int(input("Введите точку y1: "))
    y2 = int(input("Введите точку y2: "))
    y3 = int(input("Введите точку y3: "))

    return calc_triangle(x1, x2, x3, y1, y2, y3)


def calc_triangle(x1, x2, x3, y1, y2, y3):
    a = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    b = sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2))
    c = sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))

    p = (a + b + c)
    S = (p - a) * (p - b) * (p - c)

    print("Площадь равна: ", S, "\nПериметр равен: ", p)

    return True


enter_num()
