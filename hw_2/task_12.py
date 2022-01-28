def enter_num() -> float:
    start = 1000

    year = int(input("Введите год: "))
    year_x = ((year - start) % 12) + 1

    return calc_japanese_calendar(year_x)


def calc_japanese_calendar(yearx):
    if yearx == 1:
        print('Год крысы')
    elif yearx == 2:
        print('Год быка')
    elif yearx == 3:
        print('Год тигра')
    elif yearx == 4:
        print('Год заяца')
    elif yearx == 5:
        print('Год дракона')
    elif yearx == 6:
        print('Год змеи')
    elif yearx == 7:
        print('Год лошади')
    elif yearx == 8:
        print('Год овцы')
    elif yearx == 9:
        print('Год обезьяны')
    elif yearx == 10:
        print('Год петуxа')
    elif yearx == 11:
        print('Год собаки')
    elif yearx == 12:
        print('Год свиньи')

    else:
        print("неверный год")

    return True


enter_num()
