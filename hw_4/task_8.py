from random import randrange

def calc(matrix, n, m):
    b_multiply = []
    for row in matrix:
        row_b_row_b_multiply = 1
        for element in row:
            row_b_row_b_multiply *= element
        b_multiply.append(row_b_row_b_multiply)
    print(f'Произведение элементов соответствующих строк: {b_multiply}')
    b_average = []
    for column_num in range(0, n):
        column_sum = 0
        for row_num in range(0, m):
            column_sum += matrix[row_num][column_num]
        column_average = column_sum / m
        b_average.append(column_average)
    print(f'Среднее арифметическое соответствующих столбцов: {b_average}')
    b_difference = []
    for row in matrix:
        row_difference = max(row) - min(row)
        b_difference.append(row_difference)
    print(f'Разность наибольших и наименьших элементов соответствующих строк: {b_difference}')
    b_first_negative = []
    for column_num in range(0, n):
        column_negative = 0
        for row_num in range(0, m):
            num = matrix[row_num][column_num]
            if num < 0:
                column_negative = num if column_negative > num else column_negative
                break
        b_first_negative.append(column_negative)
    print(f'Значения первых отрицательных элементов в столбце(0 - если нет отриц. числа): {b_first_negative}')


n = int(input('Введите размер строки: '))
m = int(input('Введите размер столбца: '))
if n < 1 or m < 1:
    print("Введите число больше 0!")
else:
    matrix = [[randrange(-10, 10) for i in range(n)] for y in range(m)]
    for row in matrix:
        print(row)
    calc(matrix, n, m)