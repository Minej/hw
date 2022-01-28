PI = 3.14


def enter_num() -> float:
    r1 = float(input("Введите радиус нижнего основания r1: "))
    r2 = float(input("Введите радиус верхнего основания r2: "))
    l = float(input("Введите образующую l: "))
    height = float(input("Введите высоту h: "))

    return calc(r1, r2, l, height)


def calc(r1, r2, l, height):
    S = PI * (r1 + r2) * l + (PI * (r1 ** 2)) + (PI * r1)
    V = (1 / 3) * PI * (r2 ** 2 + r1 ** 2 + r2 * r1) * height

    print('Площадь усеченного конуса равна: ', S, '\nОбъем усеченного конуса равна: ', V)

    return True


enter_num()
