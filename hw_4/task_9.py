import array

n = int(input("введите размерность массива n: ", range (1, 11)))
r = int(input("Число для поиска r: " , range(-n, n), True))

abc = array[0]
for a in array:
    if abs(a - r) < abs (abc - r):
        abc = a
    else:
        abs(a - r) > abs (abc - r)
        abc = a
        