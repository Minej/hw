def calc_func():
    eps = 0.00001
    value = 1
    i = 0
    output = 0

    while value >= eps:
        i += 1
        value = 1 / i ** 2
        output += value

    return format(eps, 'f'), output


eps, output = calc_func()
print(f'Приближенное значение с точностью eps = {eps} будет равно {output}')
