def enter_num() -> float:
    x = float(input("Введите число х: "))
    y = float(input("Введите число y: "))

    if x == y:
        print("Числа равны")
    else:
        return calc(x, y)


def calc(x, y):
    min_num = min(x, y)
    max_num = max(x, y)

    half_sum = (x + y) / 2
    double_multiply = (x * y) * 2

    print(f"Меньшее из двух чисел {min_num} -> {half_sum} "
          f"\nбольшее из двух чисел {max_num} -> {double_multiply}")

    return True


enter_num()
