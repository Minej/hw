def enter_num():
    n = float(input("Введите число n: "))

    return calc(n)


def calc(n):
    output = 0
    while n > 0:
        output += 1 + (1 / n ** 2)

        n -= 1

    print(round(output, 2))

    return True


enter_num()
