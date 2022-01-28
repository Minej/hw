from math import sqrt


def enter_num() -> float:
    a = float(input("Введите данные сторону 'а' : "))
    b = float(input("Введите данные сторону 'b' : "))

    return calc_perim(a, b)


def calc_perim(a, b):
    perimeter = 2 * (a + b)
    square = a * b
    diagonal = sqrt(a * a + b * b)

    print("Перемитр равен: ", perimeter, "\nПлощадь равна: ", square, "\nДиагональ равна: ", diagonal)

    return True


enter_num()
