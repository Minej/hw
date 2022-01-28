from math import sqrt, cos, log, e


def enter_num():
    a = float(input('Введите действительное число: '))
    q = int(input('Введите целое число: '))
    t = float(input('Введите действительное число: '))

    return calc(a, q, t)


def calc(a, q, t):
    output_dict = {}

    for i in range(2, 7, 1):
        x = i * 0.1
        formula = (3 * (x ** 2) - sqrt(cos(q ** 3))) / (log(q + a, e) * t)
        output_dict[round(x, 1)] = round(formula, 4)

    return output_dict


for key, value in enter_num().items():
    print(f'При x = {key}, w = {value}')
