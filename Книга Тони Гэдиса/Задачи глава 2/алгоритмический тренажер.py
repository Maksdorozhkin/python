# height = input('Введите свой рост ')
# print(height)
# color = input('Введите свой любимый цвет ')
# print(color)

a = ('b') * 4
print(a)

w, x, y, z = 5, 4, 8, 2
rezult = x + y, z * 2, y / x, y - z, w // z
print(rezult)

total = 10 + 14
print(total)
down_payment = rezult
subtotal = 8
total = subtotal * 0.15

sales = 6.9876
print(f'{sales:.2f}')  # округление до двух десятичных

number = 1234567.5
print(f'{number:,.1f}')  # разделяет запятыми большое число и сокращает вещественное число

print('m', 'c', sep='@')  # вставляет собаку в серидину

import turtle

turtle.speed(1)
# turtle.circle(75) # рисует круг с радиусом 75
# рисуем квадрат и заполняем его синим цветом
turtle.begin_fill()
turtle.fillcolor('blue')
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()
# рисуем круг в центре квадрата и заполняем его белым
turtle.begin_fill()
turtle.fillcolor('white')
turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()
turtle.pendown()
turtle.circle(40)
turtle.end_fill()
