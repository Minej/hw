from random import randrange


def calc(matrix, n, m):
    for column_num in range(0, n):
        for row_num in range(0, m):
            matrix[row_num][column_num] = 0 if matrix[row_num][column_num] >= 0 else 1
    print('Матрица после замены:')
    for row in matrix:
        print(row)
    count_row = 0
    for row in matrix:
        matrix[count_row] = sorted(row, reverse=True)
        count_row += 1
    print('Матрица после сортировки:')
    for row in matrix:
        print(row)


n = int(input('Введите размер строки: '))
m = int(input('Введите размер столбца: '))
if n < 1 or m < 1:
    print("Введите число больше 0!")
else:
    matrix = [[randrange(-10, 10) for i in range(n)] for y in range(m)]
    for row in matrix:
        print(row)
    calc(matrix, n, m)
