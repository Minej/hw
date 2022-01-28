from math import sqrt


def get_median(x: float, y: float, z: float) -> float:
    return round((1 / 2) * (sqrt(2 * x ** 2 + 2 * y ** 2 - z ** 2)), 2)


a, b, c = [float(x) for x in input(f"Введите 3 положительных числа через пробел: ").split()]
if a < 1 or b < 1 or c < 1:
    raise ValueError('Используйте только положительные числа!')

m_of_a = get_median(b, c, a)
m_of_b = get_median(a, c, b)
m_of_c = get_median(a, b, c)

print(f"Медианы исходного треугольника: к стороне a = {m_of_a}, к стороне b = {m_of_b}, к стороне c = {m_of_c}.")

m_of_ma = get_median(m_of_b, m_of_c, m_of_a)
m_of_mb = get_median(m_of_a, m_of_c, m_of_b)
m_of_mc = get_median(m_of_a, m_of_b, m_of_c)

print(
    f"Медианы получившегося треугольника: к стороне a1 = {m_of_ma}, к стороне b1 = {m_of_mb}, к стороне c1 = {m_of_mc}.")
