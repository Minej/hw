from math import sqrt


def find_length(x1, y1, x2, y2) -> float:
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def get_area(a_x, a_y, b_x, b_y, c_x, c_y) -> float:
    segment_a = find_length(a_x, a_y, b_x, b_y)
    segment_b = find_length(b_x, b_y, c_x, c_y)
    segment_c = find_length(c_x, c_y, a_x, a_y)
    perimeter = segment_a + segment_b + segment_c
    semi_perimeter = perimeter / 2
    s = sqrt(
        semi_perimeter * (semi_perimeter - segment_a) * (semi_perimeter - segment_b) * (semi_perimeter - segment_c))
    return round(s, 2)


def get_height(area, orig_segment) -> float:
    return round((2 * area) / orig_segment, 2)


def get_min_msg(height: float, side: str):
    print(f"Расстояние от точки до ближайшей стороны треугольника = {height}, сторона {side}.")


a_x, a_y = [int(x) for x in input("Введите координаты вершины a (2 числа через пробел): ").split()]
b_x, b_y = [int(x) for x in input("Введите координаты вершины b (2 числа через пробел): ").split()]
c_x, c_y = [int(x) for x in input("Введите координаты вершины c (2 числа через пробел): ").split()]
o_x, o_y = [int(x) for x in input("Введите координаты точки o (2 числа через пробел): ").split()]

area_abo = get_area(a_x, a_y, b_x, b_y, o_x, o_y)
area_bco = get_area(b_x, b_y, c_x, c_y, o_x, o_y)
area_aco = get_area(a_x, a_y, c_x, c_y, o_x, o_y)

height_ab = get_height(area_abo, find_length(a_x, a_y, b_x, b_y))
height_bc = get_height(area_bco, find_length(b_x, b_y, c_x, c_y))
height_ac = get_height(area_aco, find_length(a_x, a_y, c_x, c_y))

min_h = min(height_ab, height_ac, height_bc)
if min_h == height_ab:
    get_min_msg(min_h, "AB")
elif min_h == height_bc:
    get_min_msg(min_h, "BC")
else:
    get_min_msg(min_h, "AC")
