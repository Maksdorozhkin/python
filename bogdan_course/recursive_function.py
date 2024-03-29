import math
# рекурсивная функция это функция внутри себя вызывает себя же, вычисляем факториал используя рекурсивную функцию


def calc_factorial(num):
    if type(num) is not int:
        raise TypeError("Number must be int ")
    if num <= 0:
        raise ValueError("Number must be > 0")
    if num == 1:
        return 1
    return calc_factorial(num - 1) * num


print(calc_factorial(10))

print(math.factorial(10))
