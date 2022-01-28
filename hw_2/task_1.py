def enter_num():
    x = float(input("Введите число х: "))
    y = float(input("Введите число у: "))

    return calc(x, y)


def calc(x, y):
    if x < 0 and y < 0:
        x = abs(x)
        y = abs(y)

    elif x < 0 or y < 0:
        x = x + 0.5
        y = y + 0.5

    elif (x > 0 and y > 0) or (x <= 0.5 and x >= 2) or (y <= 0.5 and y >= 2):
        x = x / 10
        y = y / 10

    print(f"Ответ равен: \nx => {x} \n y => {y}")

    return x, y


enter_num()
