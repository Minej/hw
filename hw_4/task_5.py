from math import ceil
from random import randrange

def calc(matrix, n):
    middle = (int(ceil(n / 2)))
    count_a = 0
    print(f'Выше главной диагонали:')
    for val in range(1, middle + 1):
        row = matrix[val - 1]
        sorted_arr = row[val - 1: n]
        print_arr = ['X' for _ in range(val - 1)]
        print_arr.append(sorted_arr)
        print(print_arr)
        count_a += sum(x == 0 for x in sorted_arr)
    for val in range(middle + 1, n + 1):
        row = matrix[val - 1]
        sorted_arr = row[val - 1: n]
        print_arr = ['X' for _ in range(val)]
        print_arr.append(sorted_arr)
        print(print_arr)
        count_a += sum(x == 0 for x in sorted_arr)
    print(f'Количество нулевых элементов: {count_a}')
    print('------------------------------')
    print(f'Ниже главной диагонали:')
    count_b = 0
    for val in range(1, middle + 1):
        row = matrix[val - 1]
        sorted_arr = row[0: val]
        print(sorted_arr)
        count_b += sum(x == 0 for x in sorted_arr)
    for val in range(middle + 1, n + 1):
        row = matrix[val - 1]
        sorted_arr = row[0: val]
        print(sorted_arr)
        count_b += sum(x == 0 for x in sorted_arr)
    print(f'Количество нулевых элементов: {count_b}')


n = int(input('Введите размерность матрицы n*n: '))
if n < 1:
    print("Введите число больше 0!")
else:
    matrix = [[randrange(-4, 4) for i in range(n)] for y in range(n)]
    for row in matrix:
        print(row)
    calc(matrix, n)