# x = int(input(' Введите число'))
# if x > 100:
#     y = 20
#     z = 40
#     print(y, z)
#
# a = int(input('Введите число для а '))
# if a < 10:
#     b = 0
#     c = 1

# a = int(input('Введите число для а '))
# if a < 10:
#     b = 0
# else:
#     b = 99
# print(b)

# 5
# крутая задача
# amount1 = int(input('Введите значение для amount1 '))
# amount2 = int(input('Введите знпчение для amount2 '))
# if amount1 > 10 and amount2 < 100:
#     if amount1 > amount2:
#         print(amount1)
#     else:
#         print(amount2)

#
# speed = int(input('Введите скорость '))
# if speed > 26 and speed < 56:
#     print('Скорость норм')
# else:
#     print('Скорость аварийная! ')


# points = int(input('Введи значение для переменной points '))
# if points > 9 and points < 51:
#     print('Допустимые точки!')
# else:
#     print('Недопустимые точки! ')

import turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

turtle.setheading(30.0)

if turtle.heading() >= 0 and turtle.heading() <= 45:
    turtle.penup()
if turtle.pencolor('red') and turtle.pencolor('blue'):
    turtle.pensize(5)

# TARGET_LEFT_X = 100
# TARGET_LEFT_Y = 100
# TARGET_RIGHT_X = 200
# TARGET_RIGHT_Y = 200
# turtle.speed(2)
# turtle.penup()
# turtle.goto(TARGET_LEFT_X, TARGET_LEFT_Y)
# turtle.setheading(0)
# turtle.pendown()
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(150)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(150)
LEFT_UP_ANGLE_X = 100
LEFT_UP_ANGLE_Y = 100
RIGHT_BOTTOM_ANGLE_X = 200
RIGHT_BOTTOM_ANGLE_Y = 200
WITH = 100
if (turtle.xcor() >= LEFT_UP_ANGLE_X
        and turtle.xcor() <= (LEFT_UP_ANGLE_X + WITH)
        and turtle.ycor() >= RIGHT_BOTTOM_ANGLE_X
        and turtle.ycor() <= (RIGHT_BOTTOM_ANGLE_Y + WITH)):
    turtle.hideturtle()
# смысл этой задачи понятен я не стал заморачиваться просто написал как это работает приблизительно
# если будет конкретная цель расчитаю точно
