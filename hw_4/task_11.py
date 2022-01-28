from random import randrange


def calc(matrix, n):
    b_row_sum = []
    b_average = []
    for row in matrix:
        b_row_sum.append(sum(row))
        b_average.append(sum(row) / n)
    print(f'Суммы элементов строк: {b_row_sum}')
    b_multiply = []
    for row in matrix:
        row_b_multiply = 1
        for element in row:
            row_b_multiply *= element
        b_multiply.append(row_b_multiply)
    print(f'Произведение элементов строк: {b_multiply}')
    print(f'Среднее арифметическое элементов строк: {b_average}')


n = int(input('Введите размер строки: '))
m = int(input('Введите размер столбца: '))
if n < 1 or m < 1:
    print("Введите число больше 0!")
else:
    matrix = [[randrange(-10, 10) for i in range(n)] for y in range(m)]
    for row in matrix:
        print(row)
    calc(matrix, n)
