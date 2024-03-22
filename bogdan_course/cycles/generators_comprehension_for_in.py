# nums = (3, 5, 10)
# squares = (num * num for num in nums)
# print(squares)
# print(type(squares))


squares1 = (num * num for num in range(10))
print(squares1)
print(type(squares1))
for num1 in squares1:
    print(num1)

# Конвертация генератора в список
n = [3, 5, 10]
gen = (n1 * n1 for n1 in n)
squares2 = list(gen)
print(squares2)
