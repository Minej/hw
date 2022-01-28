from math import factorial


def enter_num():
    x = float(input('Введите действительное число: '))
    n = int(input('Введите натуральное число: '))

    return calc(x, n)


def calc(x, n):
    counter = 1
    output = 0

    while counter <= n:
        output += (x ** counter) / (factorial(counter))
        counter += 1

    print(round(output, 2))

    return True


enter_num()
