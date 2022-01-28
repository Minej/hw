def enter_num() -> float:
    x = float(input("Введите число: "))

    return calc(x)

def calc(x):
    if x > 0:
        print("+ Число положительное")

    elif x < 0:
        print("- Число отрицательное")

    elif x == 0:
        print("Число равно нулю")

    else:
        print("Введите только лишь число")
        
    print(f"Ответ равен: {x}")
   
    return True


enter_num()

