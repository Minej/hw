def enter_num() -> float:
    x = int(input("Введите x: "))
    n = int(input("Введите n: "))

    return calc(n, x)

def calc(n, x):
    value = 1
    count = 0

    while count <= n:
        value *= x - (count * n)
        count += 1

    print(f"Ответ равен: {value}")
   
    return True


enter_num()

