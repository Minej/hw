import math

def enter_num() -> float:
    a = int(input())
    b = int(input())
    c = int(input())

    return calc_cube_params(a, b ,c)


def calc_cube_params(a, b, c):
    a = (math.sqrt(c**2 - b**2))
    b = (math.sqrt(c**2 - a**2))
    c = (math.sqrt(a**2 - b**2))


    print(f"Ответ равен: {a, b, c}")

    return True

enter_num()


