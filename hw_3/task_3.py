from math import sin


def enter_num():
    n = float(input("Введите число n: "))

    return calc(n)


def calc(n):
    output = 0
    sin_num = 0
    first = 1

    while first < n + 1:
        sin_num += sin(first)
        output += 1 / sin_num
        first += 1

    print(round(output, 2))

    return True


enter_num()
