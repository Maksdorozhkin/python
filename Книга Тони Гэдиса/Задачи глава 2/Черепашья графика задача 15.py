import turtle

# компас
turtle.speed(0)
turtle.penup()
turtle.goto(-250, -200)
turtle.pendown()
turtle.forward(100)
turtle.write('Восток')
turtle.goto(-250, -200)
turtle.left(90)
turtle.forward(100)
turtle.write('Север')
turtle.goto(-250, -200)
turtle.left(90)
turtle.forward(100)
turtle.write('Запад')
turtle.goto(-250, -200)
turtle.left(90)
turtle.forward(100)
turtle.write('Север')
turtle.penup()
turtle.goto(-270, -200)
turtle.pendown()
turtle.circle(20)

# квадрат пунктир

turtle.penup()
turtle.goto(0, -100)
turtle.dot()
turtle.pendown()
turtle.forward(200)
turtle.dot()
turtle.right(270)

turtle.forward(10)
turtle.penup()
turtle.forward(30)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.forward(40)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.forward(30)
turtle.pendown()
turtle.forward(10)
turtle.dot()
turtle.left(90)
turtle.forward(200)
turtle.dot()
turtle.left(90)
turtle.forward(10)
turtle.penup()
turtle.forward(30)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.forward(40)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.forward(30)
turtle.pendown()
turtle.forward(10)
turtle.left(135)
turtle.forward(141.42)
turtle.dot()
turtle.forward(141.42)
turtle.left(45)
turtle.penup()

turtle.left(90)
turtle.pendown()
turtle.forward(200)
turtle.left(135)
turtle.forward(282.84)

# ауди

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.circle(30)
turtle.penup()
turtle.goto(70, 100)
turtle.pendown()
turtle.circle(30)
turtle.penup()
turtle.goto(140, 100)
turtle.pendown()
turtle.circle(30)
turtle.penup()
turtle.goto(105, 65)
turtle.pendown()
turtle.circle(30)
turtle.penup()
turtle.goto(35, 65)
turtle.pendown()
turtle.circle(30)

# треугольники

turtle.penup()
turtle.goto(20, 150)
# turtle.dot()
turtle.left(135)
turtle.pendown()
turtle.forward(150)
turtle.left(180)
turtle.right(65)
turtle.forward(178)  #
turtle.penup()
turtle.goto(20, 150)
turtle.left(90)
turtle.right(140)
turtle.pendown()
turtle.forward(178)
turtle.penup()
turtle.goto(20, 150)
turtle.right(20)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.forward(100)
turtle.penup()
turtle.goto(20, 150)
turtle.right(45)
turtle.forward(150)
turtle.left(135)
turtle.pendown()
turtle.forward(108)
turtle.end_fill()

# ромб закрашенный х 2


turtle.done()
