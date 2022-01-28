vector1 = (10, range(-10, 10))
vector2 = (10, range(-10, 10))

m = print.sum(vector1)
n = print.sum(vector2)

def sum(vector):
    if len(vector1 or vector2) == 0:
        return 0
    negativ = [i for i in vector if i <0]
    return sum([i ** 2 for i in negativ])

def get_x (m: int, n: int) -> float:
    return round(m / (n - m), 2)
        
