from random import randrange


def calc(arr, n):
    arr_even = arr[::2]
    arr_odd = arr[1::2]
    res_arr = [None] * n
    count_even = 0
    count_odd = 1
    for var in arr_even:
        if n <= count_odd:
            res_arr[n - 1] = var
            break
        res_arr[count_odd] = var
        count_odd += 2
    for var in arr_odd:
        res_arr[count_even] = var
        count_even += 2
    print(f'Переставленный массив: {res_arr}')


n = int(input('Введите кол-во элементов в массиве: '))
if n < 1:
    print("Введите число больше 0!")
else:
    arr = [randrange(-10, 10) for i in range(n)]
    print(f'Массив: {arr}')
    calc(arr, n)
