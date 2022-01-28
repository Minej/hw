import random
import string


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print('----------------------------------------------')


def get_rand_matrix(number) -> [[]]:
    return [[random.choice('abcde' + string.octdigits) for _ in range(number)] for y in range(number)]


def input_positive_number() -> int:
    num = int(input('Введите размерность матрицы n*n: '))
    if num < 1:
        raise ValueError("Введите число больше 0!")
    return num


def find_vowel(matrix, len_matrix):
    for i in range(len_matrix):  
        for j in range(len_matrix):  
            letter = matrix[i][j]
            if letter == 'a' or letter == 'e':
                return True
    return False


def transpose_matrix(matrix, len_matrix):
    trans_matrix = [[0 for _ in range(len_matrix)] for _ in range(len_matrix)] 
    for i in range(len_matrix):  
        for j in range(len_matrix):  
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


def is_digital_diagonal(matrix, len_matrix) -> []:
    diagonal = []
    for val in range(len_matrix):
        if str(matrix[val][val]).isdigit():
            diagonal.append(matrix[val][val])
    return len(diagonal) == len_matrix, diagonal


def b_case_matrix(diagonal_arr, orig_matrix) -> [[]]:
    min_val = min(diagonal_arr)
    copy_matrix = orig_matrix[:]
    for it in range(len(diagonal_arr)):
        if min_val == diagonal_arr[it]:
            copy_matrix.remove(orig_matrix[it])
    return copy_matrix


pos_num = input_positive_number()
for i in range(3):
    new_matrix = get_rand_matrix(pos_num)
    print(f'Матрица #{i + 1}:')
    print_matrix(new_matrix)
    if find_vowel(new_matrix, pos_num):
        transposed_matrix = transpose_matrix(new_matrix, pos_num)
        print(f'Транспонированная матрица {i + 1}:')
        print_matrix(transposed_matrix)
    exec_b_case, diagonal = is_digital_diagonal(new_matrix, pos_num)
    if exec_b_case:
        changed_matrix = b_case_matrix(diagonal, new_matrix)
        print(f'Матрица {i + 1} с удаленной строкой, где было минимальное значение по диагонали:')
        print_matrix(changed_matrix)
