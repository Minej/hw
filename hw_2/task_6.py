def enter_num() -> float:
    x1 = float(input("Введите первое число: "))
    x2 = float(input("Введите второе число: "))
    operation = input("Введите какой знак вы хотите использовать? (+, -, /, *): ")

    return calc(x1, x2, operation)


def calc(x1, x2, operation):
    if operation == "-":
        print(x1 - x2)

    elif operation == "+":
        print(x1 + x2)

    elif operation == "/":
        if x2 != 0:
            print(x1 / x2)
        else:
            print("На ноль делить нельзя")

    elif operation == "*":
        print(x1 * x2)

    else:
        print("Неверный знак, введите зановo")

    return True


enter_num()
