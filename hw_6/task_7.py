from random import randrange


def count_numbers(array: [], number: float) -> int:
    return sum(1 for i in array if i > number)


num = float(input("Введите число: "))
arr = [randrange(-20, 20) for i in range(20)]
print(arr)
print(f'Количество чисел в массиве, которые больше числа {num}: {count_numbers(arr, num)}')
