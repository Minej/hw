from math import sqrt


def enter_num() -> float:
    initial_velocity = float(input("Введите начальную скрость: "))
    time = float(input("Введите время проохождения: "))
    acceleration = float(input("Введите ускорения тела: "))

    return calc_distance(initial_velocity, time, acceleration)


def calc_distance(initial_velocity, time, acceleration):
    distance = initial_velocity * time + (acceleration * sqrt(time) / 2)

    print(f"Расстояние равна: {distance}")

    return True


enter_num()
