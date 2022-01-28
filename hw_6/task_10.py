def is_repeat(number: int) -> bool:
    seen = []
    for digit in str(number):
        if digit in seen:
            return True
        seen.append(digit)
    return False


unique_arr = []
for value in range(1000, 10000):
    if not is_repeat(value):
        unique_arr.append(value)

print('Все четырехзначные числа, в которых цифры не повторяются:')
for index in range(0, len(unique_arr), 42):
    print(unique_arr[index:index + 42])
