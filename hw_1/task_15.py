from math import sqrt


def enter_num() -> float:
    x1 = float(input("Введите точку x1: "))
    x2 = float(input("Введите точку x2: "))
    y1 = float(input("Введите точку y1: "))
    y2 = float(input("Введите точку y2: "))

    return calc_circle(x1, x2, y1, y2)


def calc_circle(x1, x2, y1, y2):
    distance = round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

    print(f"Расстояния между двумя точками равна: {distance}")

    return True


enter_num()
