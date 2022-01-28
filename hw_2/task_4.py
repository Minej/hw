import math


def enter_num() -> float:
    x = float(input("Введите число х: "))
    t1 = float(input("Введите число t1: "))
    t2 = float(input("Введите число t2: "))

    return calc_func(x, t1, t2)


def calc_func(x, t1, t2):
    if t1 < math.sqrt(t2 + 2):
        output = round(pow(math.e, 2 * t1) + math.cos(x * t2), 4)
    elif t1 > math.sqrt(t2 + 2):
        output = round(x * t1, 4)
    else:
        output = round(math.log(x * t1, math.e) * math.sqrt(math.sin(t2)), 4)

    print(f"Ответ равен: {output}")

    return True


enter_num()
