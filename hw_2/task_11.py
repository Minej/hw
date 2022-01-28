def enter_num() -> float:
    x1 = int(input("Введите х1: "))
    y1 = int(input("Введите y1: "))
    x2 = int(input("Введите х2: "))
    y2 = int(input("Введите y2: "))

    return calc(x1, x2, y1, y2)


def calc(x1, x2, y1, y2):
    if (x1 * x1 + y1 * y1) < (x2 * x2 + y2 * y2):
        print("Ближе к началу координат точка", x1, y1)
    elif (x1 * x1 + y1 * y1) > (x2 * x2 + y2 * y2):
        print("Ближе к началу координат точка", x2, y2)
    else:
        print("Точки равноудалены от начала координат")

    return True


enter_num()
