# def hi(name):
#     print('Hello there!', name)
#     print('Hi there!', name)
#
#
# hi('Maks') # вызов функции
# hi('Galya')

def sum_numbs(a, b):
    sum = a + b
    return (sum)
    print('Line is not executed')


first_sum = sum_numbs(10, 5)
print(first_sum)
print(sum_numbs(50.5, 20))


#
# print(sum_numbs(sum_numbs(50.5, 20),30))

# Динамическая типизация пример

def print_name(name):
    print(name)


print_name('Maks')

# далее  меняем print_name на число
print_name = 10

# и снова вызываем функцию
print_name('Maks')

# такой код выдаст ошибку т.к. print_name теперь числ
