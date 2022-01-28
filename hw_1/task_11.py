def enter_num() -> float:
    a = int(input("Введите точку a: "))
    b = int(input("Введите точку b: "))
    c = int(input("Введите точку c: "))

    return calc_func(a, b, c)


def calc_func(a, b, c):
    x = -b / (2 * a)
    y = a * (x ** 2) + (b * x) + c

    print(f"Вершины точек равна: \nx => {x} \ny => {y}")

    return True


enter_num()
