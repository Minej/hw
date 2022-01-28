from math import exp, pi, sin


def enter_num() -> float:
    a = float(input("Введите число a: "))
    omega = float(input("Введите омегу ω: "))

    return calc_func(a, omega)


def calc_func(a, omega):
    phi = (1 + 5 ** 0.5) / 2
    x = round((((pi / 2) * phi) / omega), 2)
    output = round((a * exp(-a * x) * sin(omega * x)), 4)

    print("Значение функции: ", output)

    return True


enter_num()
