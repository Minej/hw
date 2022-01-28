EXP = 2.71828


def enter_num():
    a = float(input("Введите 'a' число: "))
    b = float(input("Введите 'b' число: "))
    c = float(input("Введите 'c' число: "))

    return calc(a, b, c)


def calc(a, b, c):
    # input values  
    if (c != 0):
        x1 = (b + (abs(b ** 2 - 4 * a * c) ** 1 / 2)) / 2 * a
        x2 = (b - (abs(b ** 2 - 4 * a * c) ** 1 / 2)) / 2 * a

        # y=(EXP**(-x1)+EXP**(-x2))/2
        # z=(a*(x1**1/2)-b*(x2**1/2))/c
        # or
        y = (1 / EXP ** x1 + 1 / EXP ** x2) / 2
        z = (a * (x1 ** 1 / 2) - b * (x2 ** 1 / 2)) / c

        print(f"y = {y} \nz = {z}")
    else:
        print('division by zero')


enter_num()

# OverflowError: (34, 'Numerical result out of range')
# когда даны большие числа, это может быть решено, если тип float / int изменится на десятичные
