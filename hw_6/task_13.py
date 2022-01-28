from math import prod
from random import randrange


def multiply_odd(arr: []) -> int:
    print(arr[::2])
    return prod(arr[::2])


arr_one = [randrange(1, 10) for _ in range(10)]
print(arr_one)
arr_two = [randrange(1, 10) for _ in range(10)]
print(arr_two)
print("Произведение элементов двух массивов, стоящих на нечетных позициях")
num_one = multiply_odd(arr_one)
num_two = multiply_odd(arr_two)
print(f'{num_one} X {num_two} = {num_one*num_two}')
