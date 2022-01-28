from math import sin, sqrt, e


def enter_num():
    a = float(input('Введите действительное число: '))
    Z = int(input('Введите целое число: '))
    y = float(input('Введите действительное число: '))

    return calc(a, Z, y)


def calc(a, Z, y):
    output_dict = dict()
    x = 1
    while x <= 4.5:
        w = (a * x ** 2 + sin(Z) ** 2) / (sqrt(1 + e ** y))
        output_dict[x] = round(w, 4)
        x += 0.5
    return output_dict


for key, value in enter_num().items():
    print(f'При x = {key}, w = {value}')
