# lambda functions пример использования и синтаксис
# однострочная функция

# def mult(a, b):
#     return a * b

# пример lambda функции, возвращает 
# lambda a,b: a*b

# обычная
def mult(a, b): return a * b


print(mult(10, 5))


# пример использования lambda функции в обычной, замыкание


def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting("Good Morning")
print(morning_greeting('Maks'))

evening_greeting = greeting("Good Evening")

print(evening_greeting('Maks'))


def moto(blabla):
    return lambda bike: f"{blabla}, {bike}!"


my_blabla = moto("I love my bike")
print(my_blabla('Ducati'))
