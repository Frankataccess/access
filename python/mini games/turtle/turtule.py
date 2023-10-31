import turtle

BLUE = "#0000ff"
PINK = "#ff00ff"
GREEN = "#00ff00"
RED = "#FF0000"

def drawSquare(size, colour):
    turtle.color(colour)
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

turtle.speed(5)
turtle.setheading(0)
turtle.pendown()
drawSquare(100,BLUE)
turtle.penup()
turtle.forward(5)
turtle.right(90)
turtle.forward(5)
turtle.left(90)
turtle.pendown()
drawSquare(80, GREEN)

turtle.exitonclick