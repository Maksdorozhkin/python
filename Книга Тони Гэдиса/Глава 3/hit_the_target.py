# игра порази цель
import turtle

# константы
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25  # ширина цели
FORSE_FACTOR = 30  # Фактор произвольной силы
PROJECTILE_SPEED = 1  # скорость анимации снаряда
NORD = 90
SOUTH = 270
EAST = 0
WEST = 180

# настроить окно
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
# настроить цель
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORD)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# центровать черепаху

turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# получить угол выстрела и силу от пользователя

angle = float(input("Введите угол выстрела снаряда: "))
forse = float(input("Введите пусковую силу (1 -10): "))

# расчитать растояние
distance = forse * FORSE_FACTOR

# задать направление

turtle.setheading(angle)

# запустить снаряд

turtle.pendown()
turtle.forward(distance)

# снаряд поразил цель?

if (turtle.xcor() >= TARGET_LLEFT_X and
        turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
        turtle.ycor() >= TARGET_LLEFT_Y and
        turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Целль поражена')
else:
    print('Вы промахнулись.')
