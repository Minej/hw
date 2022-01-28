def enter_num() -> float:
    x1 = float(input("Введите x1: "))
    x2 = float(input("Введите x2: "))
    x3 = float(input("Введите x3: "))
    y1 = float(input("Введите y1: "))
    y2 = float(input("Введите y2: "))
    y3 = float(input("Введите y3: "))
    m1 = float(input("Введите m1: "))
    m2 = float(input("Введите m2: "))
    m3 = float(input("Введите m3: "))

    return calc(x1, x2, x3, y1, y2, y3, m1, m2, m3)


def calc(x1, x2, x3, y1, y2, y3, m1, m2, m3):
    x0 = round((m1 * x1 + m2 * x2 + m3 * x3) / (m1 + m2 + m3), 2)
    y0 = round((m1 * y1 + m2 * y2 + m3 * y3) / (m1 + m2 + m3), 2)

    print(f"Координаты центра тяжести равна: {x0, y0}")

    return True


enter_num()
