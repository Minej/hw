def calc():
    eps = 0.00001
    i = 1
    n = 3
    output = 0

    while True:
        value = 1 / (i * n)
        if abs(value) < eps:
            break

        output += value
        i += 1
        n += 1

    return format(eps, 'f'), output


eps, result = calc()
print(f'Значение eps: {eps} \n результат: {result}')
