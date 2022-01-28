def enter_num() -> float:
    x1 = float(input("Введите x1: "))
    x2 = float(input("Введите x2: "))
    y1 = float(input("Введите y1: "))
    y2 = float(input("Введите y2: "))
    n1 = float(input("Введите m1: "))
    n2 = float(input("Введите m2: "))

    return calculate_point_coordinates(x1, x2, y1, y2, n1, n2)


def calculate_point_coordinates(x1, x2, y1, y2, n1, n2):
    n = n1 / n2
    x = round((x1 + (n * x2)) / (1 + n), 2)
    y = round((y1 + (n * y2)) / (1 + n), 2)

    print(f"Координаты точки равны: \nx => {x} \ny => {y}")

    return True


enter_num()
