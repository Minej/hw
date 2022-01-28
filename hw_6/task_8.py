from math import sqrt


def Plo(x, y, z):
    if x < y + z and y < x + z and z < y + x:
        perimeter = x + y + z
        semi_perimeter = perimeter / 2
        s = round(sqrt(semi_perimeter * (semi_perimeter - x) * (semi_perimeter - y) * (semi_perimeter - z)), 2)
        print(f'Площадь треугольника со сторонами {x}, {y} и {z} равна {s}')
    else:
        print(f'Треугольника со сторонами {x}, {y} и {z} не существует!')


a, b, c, d = [float(x) for x in input(f"Введите 4 положительных числа через пробел: ").split()]
if a < 1 or b < 1 or c < 1 or d < 1:
    raise ValueError('Используйте только положительные числа!')

Plo(a, b, c)
Plo(a, b, d)
Plo(a, c, d)
Plo(b, c, d)
