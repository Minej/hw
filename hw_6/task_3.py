from math import sqrt


def find_length(x1, y1, x2, y2) -> float:
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def find_perimeter(*params):
    return sum([x for x in params])


def input_coordinates(letter):
    return [int(x) for x in input(f"Введите координаты вершины {letter} (2 числа через пробел): ").split()]


ax, ay = input_coordinates('a')
bx, by = input_coordinates('b')
cx, cy = input_coordinates('c')
dx, dy = input_coordinates('d')
ex, ey = input_coordinates('e')
fx, fy = input_coordinates('f')
gx, gy = input_coordinates('g')
hx, hy = input_coordinates('h')
ix, iy = input_coordinates('i')
jx, jy = input_coordinates('j')

segment_a = find_length(ax, ay, bx, by)
segment_b = find_length(bx, by, cx, cy)
segment_c = find_length(cx, cy, dx, dy)
segment_d = find_length(dx, dy, ex, ey)
segment_e = find_length(ex, ey, fx, fy)
segment_f = find_length(fx, fy, gx, gy)
segment_g = find_length(gx, gy, hx, hy)
segment_h = find_length(hx, hy, ix, iy)
segment_i = find_length(ix, iy, jx, jy)
segment_j = find_length(jx, jy, ax, ay)

perimeter_round = round(find_perimeter(segment_a, segment_b, segment_c, segment_d, segment_e, segment_f, segment_g,
                                       segment_h, segment_i, segment_j), 2)
print(f"Периметр десятиугольника:{perimeter_round}")
