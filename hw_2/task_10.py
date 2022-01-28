import math


def enter_num():
    x = int(input("Введите число х: "))

    return calc(x)


def calc(x):
    a = round((1 / (x + 5)) - (1 / (x - 9)), 2)
    b = round(math.cos(x), 2) if x >= 0 else round(math.sin(x), 2)

    y = round(math.sqrt(a + b))

    print(f"значение функции Y: {y}")

    return True


enter_num()
