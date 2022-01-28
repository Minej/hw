from random import randrange


def calc(matrix, n):
    print('Матрица после замены:')
    for row in matrix:
        index_negative_start = 0
        for index_current_element in range(n):
            if row[index_current_element] >= 0:
                temp_value = row[index_current_element]
                index_for_swap = index_current_element
                while index_for_swap > index_negative_start:
                    row[index_for_swap] = row[index_for_swap - 1]
                    index_for_swap -= 1
                row[index_negative_start] = temp_value
                index_negative_start += 1
        print(row)


n = int(input('Введите размер строки: '))
m = int(input('Введите размер столбца: '))
if n < 1 or m < 1:
    print("Введите число больше 0!")
else:
    matrix = [[randrange(-10, 10) for i in range(n)] for y in range(m)]
    for row in matrix:
        print(row)
    calc(matrix, n)
