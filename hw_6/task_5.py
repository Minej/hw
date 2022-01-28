from math import sqrt


def find_area(segment_a, segment_b, segment_c):
    perimeter = segment_a + segment_b + segment_c
    semi_perimeter = perimeter / 2
    s = sqrt(
        semi_perimeter * (semi_perimeter - segment_a) * (semi_perimeter - segment_b) * (semi_perimeter - segment_c))
    return s


a, b, c, d, e = [float(x) for x in input("Введите 5 действительных чисел через пробел: ").split()]
g, f = [float(x) for x in
        input("Введите 2 действительных чисел через пробел (отрезки, которые делят пятиугольник): ").split()]

pentagon_area = find_area(a, b, f)
pentagon_area += find_area(f, g, e)
pentagon_area += find_area(c, g, d)

print(f"Площадь пятиугольника: {round(pentagon_area, 2)}")
