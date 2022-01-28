def enter_num() -> float:
    x = int(input("Введите х: "))
    y = int(input("Введите y: "))

    return calc(x, y)


def calc(x, y):
    if x > 0 and y > 0:
        print("Точка в первой четверти")
    if x < 0 and y > 0:
        print("Точка в второй четверти")
    if x < 0 and y < 0:
        print("Точка в третьей четверти")
    if x > 0 and y < 0:
        print("Точка в четвертой четверти")
    if x == 0 and y == 0:
        print("Точка в начале координат")
    if x == 0 and y > 0:
        print("Точка на оси Х")
    if x == 0 and y < 0:
        print("Точка на оси Х")
    if x > 0 and y == 0:
        print("Точка на оси Y")
    if x < 0 and y == 0:
        print("Точка на оси Y")

    print(f"Ответ равен: {x, y}")

    return True


enter_num()
