from random import random
N = 100
a = []
for i in range(N):
    n = int(random() * 10) - 5
    a.append(n)
print(a)
s = q = 0
for i in range(N):
    if a[i] > 0:
        s += a[i]
        q += 1  
print("%5.2f" % (s/q))