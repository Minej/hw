def calc_month(x):
    next = 1 if x == 12 else x + 1

    if next == 1:
        return "Январь"
    elif next == 2:
        return 'Февраль'
    elif next == 3:
        return 'Март'
    elif next == 4:
        return 'Апрель'
    elif next == 5:
        return 'Май'
    elif next == 6:
        return 'Июнь'
    elif next == 7:
        return 'Июль'
    elif next == 8:
        return 'Август'
    elif next == 9:
        return 'Сентябрь'
    elif next == 10:
        return 'Октябрь'
    elif next == 11:
        return 'Ноябрь'
    return 'Декабрь'

x = int(input("Введите номер месяца: "))

if x in range(1, 13, 1):
    name = calc_month(x)
    print(f"Следующий месяц: {name}")
else:
    print(f"Вы ввели не правильный месяц")


