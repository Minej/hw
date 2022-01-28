def enter_num() -> float:
    r1 = float(input("Первое сопротивления: "))
    r2 = float(input("Второе сопротивления: "))
    r3 = float(input("Третье сопротивления: "))

    return calc_resistance(r1, r2, r3)


def calc_resistance(r1, r2, r3):
    resistance = (r1 * r2 * r3) / (r2 * r3 + r1 * r3 + r2 * r1)

    print(f"Сопротивление соединения: {resistance}")

    return True


enter_num()
