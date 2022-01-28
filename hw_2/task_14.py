def enter_num() -> int:
    x = int(input("Введите х: "))
    y = int(input("Введите y: "))
    r = int(input("Введите радиус: "))

    return calc(x, y, r)


def calc(x, y, r):
    x0 = y0 = 0

    if (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:
        print("Попадает")
    else:
        print("Не попадает")

    return True


enter_num()
