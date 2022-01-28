from math import factorial, e


def calc(x):
    eps = 0.00001
    i = 1
    output = 1

    while True:
        value = (x ** i) / factorial(i)
        if abs(value) < eps:
            break
        output += value
        i += 1

    return format(eps, 'f'), output


x = int(input('Введите число: '))
eps, output = calc(x)
print(f'Значение eps: {eps} \nОтвет: {output}')
