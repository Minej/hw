from random import randrange


def calc(arr):
    seen = []
    duplicates = dict()
    for val in arr:
        if val in seen:
            if val not in duplicates:
                duplicates[val] = 1
            duplicates[val] += 1
        else:
            seen.append(val)
    print('Результат:')
    for key, value in duplicates.items():
        print(f'{key} дублируется {value} раз(-а).')
    max_value = max(duplicates.values())
    max_keys = [k for k, v in duplicates.items() if v == max_value]
    print(f'наибольшее число повторений у элементов(-а): {max_keys}. Его/их кол-во повторений: {max_value}')


n = int(input('Введите кол-во элементов в массиве: '))
if n < 1:
    print("Введите число больше 0!")
else:
    arr = [randrange(-10, 10) for i in range(n)]
    print(f'Массив: {arr}')
    calc(arr)
