def enter_num() -> float:
    x = float(input('Введите действительное число: '))
    n = int(input('Введите натуральное число: '))

    return calc(n, x)


def calc(n, x):
    counter = 1
    output_x = x
    output = 0

    while counter <= n + 1:
        output += 1 / output_x
        output_x *= x + counter
        counter += 1

    print(round(output, 2))

    return True


enter_num()
