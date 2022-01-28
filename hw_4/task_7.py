one_hundred_integer_list = [1, 34, 89, 35, 0, 11, 3]

big_int = max(one_hundred_integer_list)
min_int = min(one_hundred_integer_list)

summ = 0
for i in range(min_int, big_int + 1):
    summ += i

print(summ)
