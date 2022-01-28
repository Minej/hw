def enter_num() -> float:
    x = int(input("Введите число х: "))
    y = int(input("Введите число y: "))
    z = int(input("Введите число z: "))

    return calc(x, y, z)


def calc(x, y, z):
    if ((x + y) < z):
        print("Треугольник несуществует")
    elif ((x + z) < y):
        print("Треугольник несуществует")
    elif ((z + y) < x):
        print("Треугольник несуществует")
    else:
        print("Треугольник существует")

    return True


enter_num()
