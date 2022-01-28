from math import pi


def enter_num() -> float:
    radius = float(input("Введите радиус: "))
    height = float(input("Введите высоту: "))

    return calc_func(radius, height)


def calc_func(r, h):
    square = round((2 * pi * r * (h + r)), 2)

    print(f"Площадь поверхности цилиндра: {square}")

    return True


enter_num()
