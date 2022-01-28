PI = 3.14


def enter_num() -> float:
    l = float(input("Введите длину: "))

    return calc_circle(l)


def calc_circle(l):
    radius = l / 2 * 3.14
    square = PI * (radius ** 2)

    print(f"Площадь круга: {square}")

    return True


enter_num()
