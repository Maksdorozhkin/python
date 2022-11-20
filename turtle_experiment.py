import turtle

turtle.setup(640, 480)
turtle.shape('turtle')  # вид черепахи
turtle.shapesize(1)
turtle.bgcolor('gray')
turtle.pensize(1.5)
turtle.pencolor('yellow')
turtle.speed(1)

# radius = turtle.numinput('Введите данные', 'Введи диаметр от 1 до 10', default=30, minval=1, maxval=100)
# turtle.circle(radius)

# name = turtle.textinput('Введите данные', 'Ведите свое имя')
# print(name.title())


turtle.done()  # оставляет окно открытым
