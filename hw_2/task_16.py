from math import sin, cos, sqrt


def enter_num():
    x = float(input("Введите число х: "))

    return calc(x)


def calc(x):
    a = cos(x) if x >= 0 else sin(x)
    b = sqrt(1 / x + 1)

    y = 1 / (a + b) if a <= b else a + sqrt(b)

    print(f"Значение функции Y: {y}")

    return True


enter_num()
