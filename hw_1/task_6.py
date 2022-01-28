from math import sqrt


def enter_num() -> float:
    a = float(input("Введите значения: "))
    b = float(input("Введите значения: "))
    c = float(input("Введите значения: "))

    return calc_triangle(a, b, c)


def calc_triangle(a, b, c):
    half_perim = (a + b + c) / 2
    height = (2 / a) * sqrt(half_perim * (half_perim - a) * (half_perim - b) * (half_perim - c))

    print(f"Bысотa треугольника: {height}")

    return True


enter_num()
