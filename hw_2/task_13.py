PI = 3.14


def enter_num() -> int:
    a = int(input("Введите сторону квадрата: "))
    radius = int(input("Введите радиус окружности: "))

    return calc_square(a, radius)


def calc_square(a, radius):
    s_circle = PI * radius * radius
    s_square = a * a

    output = f"Круг: {s_circle}" if s_circle > s_square else f"Квадрат: {s_square}"

    print(output)

    return True


enter_num()
