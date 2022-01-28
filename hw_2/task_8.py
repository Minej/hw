import math


def enter_num():
    x = int(input("Введите x: "))

    return calc(x)


def calc(x):
    a = math.sin(x)
    b = math.cos(x)
    c = math.log10(x)

    min_val = min(a, b, c)

    print(f"Минимальное значение х: {min_val}")

    return True


enter_num()
