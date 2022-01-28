from math import sin, sqrt, e


def enter_num():
    a = float(input('Введите действительное число: '))
    q = int(input('Введите целое число: '))
    t = float(input('Введите действительное число: '))

    return calc(a, q, t)


def calc(a, q, t):
    output_dict = {}

    for i in range(5, 11, 1):
        z = i * 0.1
        formula = (sin((z + a) ** 3) ** 2) / (t * sqrt(e ** (a + 2 * q)))
        output_dict[round(z, 1)] = round(formula, 4)

    return output_dict


for key, value in enter_num().items():
    print(f'При x = {key}, w = {value}')
