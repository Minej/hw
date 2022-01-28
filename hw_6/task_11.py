from math import sqrt


def get_area(a_x, a_y, b_x, b_y, c_x, c_y):
    a_b = sqrt(((b_x - a_x) ** 2) + ((b_y - a_y) ** 2))
    b_c = sqrt(((c_x - b_x) ** 2) + ((c_y - b_y) ** 2))
    a_c = sqrt(((c_x - a_x) ** 2) + ((c_y - a_y) ** 2))
    perimeter = a_b + b_c + a_c
    semi_perimeter = perimeter / 2
    s = sqrt(semi_perimeter * (semi_perimeter - a_b) * (semi_perimeter - b_c) * (semi_perimeter - a_c))
    return round(s, 2)


def get_triangle_area(num: int):
    a_x, a_y = [int(x) for x in input(f"Введите координаты вершины a для треугольника #{num} "
                                      f"(2 числа через пробел): ").split()]
    b_x, b_y = [int(x) for x in input(f"Введите координаты вершины b для треугольника #{num} "
                                      f"(2 числа через пробел): ").split()]
    c_x, c_y = [int(x) for x in input(f"Введите координаты вершины c для треугольника #{num} "
                                      f"(2 числа через пробел): ").split()]
    s = get_area(a_x, a_y, b_x, b_y, c_x, c_y)
    return s


s1 = get_triangle_area(1)
s2 = get_triangle_area(2)

biggest_tr, biggest_area, smallest_tr, smallest_area = (1, s1, 2, s2) if s1 > s2 else (2, s2, 1, s1)
print(f"Площадь треугольника #{biggest_tr} = {biggest_area} имеет большую площадь, "
      f"чем площадь треугольника #{smallest_tr} = {smallest_area}")
