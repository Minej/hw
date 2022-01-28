from random import randrange


def random_arrays():
    arr1 = [randrange(-10, 0) for _ in range(10)]
    arr2 = [randrange(-10, 0) for _ in range(10)]

    return calc(arr1, arr2)


def calc(arr1, arr2):
    m = sum([_ ** 2 for _ in arr1])
    n = sum([_ ** 2 for _ in arr2])

    X = m / (n - m)

    print(f'Первый вектор: {arr1}')
    print(f'Второй вектор: {arr2}')
    print(f'Ответ: {X}')


random_arrays()
