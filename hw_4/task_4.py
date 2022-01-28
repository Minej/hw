def enter_num():
    a = int(input("Введите последовательность целых чисел: "))

    return calc(a)


def calc(a):
    
    #Максимальное число
    max_number = 0
    for number in a:
        if number > max_number:
            max_number = number
    print(max_number)
        
    #Сумма чисел

    sum = 0
    for number in a:
        sum += number
    print(sum)

    #среднее арифметическое

    sum = 0
    for number in a:
        sum += number
    print(sum / len(a))

    return True

enter_num()

