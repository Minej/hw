def enter_num():
    numbers = []
    while True:
        n = int(input('Введите числа и 0 в конце: '))
        if n == 0:
            break
        numbers.append(n)

    return calc(numbers)


def calc(numbers):
    max_num = max(numbers)
    sum_num = sum(numbers)
    average = sum_num / len(numbers)

    print(f'максимальное число: {max_num}, сумма всех чисел: {sum_num}, среднее арифметическое: {average}')

    return True


enter_num()
