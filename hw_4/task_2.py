from random import randrange


def enter_array_el_num():
    n = int(input("Введите n: "))

    return random_array(n)


def random_array(n):
    arr = [randrange(-10, 20) for _ in range(n)]
    print(arr)
    return calc(arr)


def calc(arr):
    arr_len = len(arr)
    sum_els = sum(arr)
    average = sum_els / arr_len

    counter = 1

    for num in arr:
        if num > 0:
            counter *= num

    print(
        f"Сумма элементов: {arr_len} \nСреднее арифметическое {average}  \nПроизведение положительных элементов {counter} ")

    return True


enter_array_el_num()
