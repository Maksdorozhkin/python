# области видимости переменных
a = 10  # глобальная переменная


def my_fn():
    a = True
    b = 15  # переменная внутри функции
    print(a)
    print(b)


my_fn()

print(a)


# print(b)

def my_fn2():
    """
Создание глобальной переменной внутри функции, функцию нужно вызвать
    """
    global a
    a = 10


my_fn2()

print(a)


def my_fn3(f, g):
    d = 100
    print(f, g)
    print(dir())


my_fn3(3, 5)
print(dir())
