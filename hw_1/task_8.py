PI = 3.14


def enter_num() -> float:
    height = float(input("Введите высоту: "))
    radius = float(input("Введите радиус: "))

    return calc_cube_params(height, radius)


def calc_cube_params(height, radius):
    s = 2 * PI * radius * (height + radius)

    print(f"Полная поверхность цилиндра равна: {s}")

    return True


enter_num()
