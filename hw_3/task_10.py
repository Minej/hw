from math import cos, log, e, sqrt


def enter_num():
    b = float(input('Введите действительное число: '))
    q = int(input('Введите целое число: '))
    y = float(input('Введите действительное число: '))

    return calc(b, q, y)


def calc(b, q, y):
    output_dict = dict()
    counter = 1

    while counter <= 5:
        t = (b ** 2 + sqrt(abs(q))) / (cos(counter) ** 2 + b * log(y, e))
        output_dict[counter] = round(t, 4)
        counter += 1

    return output_dict


for key, value in enter_num().items():
    print(f'При x = {key}, w = {value}')
