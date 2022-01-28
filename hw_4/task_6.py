import random
from functools import reduce
 
mas = [random.randint(-20, 20) for _ in range(15)]
print(mas)
numNeg = len(list(filter(lambda x: x < 0, mas)))
print(numNeg)
multPos = reduce(lambda x,y: x * y, filter(lambda x: x > 0, mas))
print(multPos)
null =  mas.count(0)
print(null)