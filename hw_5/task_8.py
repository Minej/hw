def enter_num() -> float:
    a = input()

    return calc_cube_params(a)


def calc_cube_params(a):
    if "А" in a or "а" in a:
        print("есть буква А")
        print(a.count("А"))
        print(a.count("а"))

    return True

enter_num()
