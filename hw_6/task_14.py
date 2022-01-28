def get_max(x: float, y: float) -> float:
    return max(x, y)


a, b, c, d = [float(x) for x in input("Введите четыре числа через пробел: ").split()]
print(f'Максимальное число: {get_max(get_max(a, b), get_max(c, d))}')
