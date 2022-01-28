def enter_num() -> float:
    a = float(input("Введите длину ребра: "))

    return calc_cube_params(a)


def calc_cube_params(a):
    volume = a ** 3
    surface = (a ** 2) * 4

    print(f"Объем равен: {volume} \nПлощадь боковой поверхности равна: {surface}")

    return True


enter_num()
