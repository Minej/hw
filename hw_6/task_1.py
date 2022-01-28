def enter_num() -> float:
    x = [ 0, 3, -3, 6, 1, 5, -2]

    s = 0
    n = len(x)

    return calc_cube_params(s, n, x)


def calc_cube_params(s, n, x):
    for k in range(n):
      if x[k]>0:
        s += x[k]
        print(s)

    return True

enter_num()
