from random import randrange

def calc(matrix, n):
    arr = []
    for row in matrix:
        average = round(sum(row) / n, 2)
        arr.append(average)
    return arr



n = int(input('Введите размер строки: '))
m = int(input('Введите размер столбца: '))
if n < 1 or m < 1:
    print("Введите число больше 0!")
else:
    matrix = [[randrange(-10, 10) for i in range(n)] for y in range(m)]
    for row in matrix:
        print(row)
    average_arr = calc(matrix, n)
    print(f'Массив из сред. арифм. каждой строки матрицы: {average_arr}')