def grow(arr):
    n = 1
    for el in arr:
        n *= el
    return n


arr = [1, 2, 3, 4]

print(grow(arr))

# перемножить все числа списка

import math


def grow(arr):
    return math.prod(arr)

