from math import factorial


def enter_num():
    n = int(input('Введите натуральное число: '))

    return calc(n)


def calc(n):
    counter = 1
    output = 1

    while counter <= n:
        output *= (2 + 1 / factorial(counter))
        counter += 1

    print(round(output, 2))

    return True


enter_num()
