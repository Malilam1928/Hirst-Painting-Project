import turtle
from turtle import Turtle, Screen
from colors import color_list
import random

"#Setting turtle attributes"

turtle.colormode(255)
pointer = Turtle()
pointer.color("white")
pointer.pencolor("white")
pointer.setheading(225)
pointer.forward(300)
pointer.setheading(0)
pointer.speed("fastest")
pointer.penup()
pointer.hideturtle()

"#Shifting each row upside at the end of the each steps"


def row_shifting():
    pointer.setheading(90)
    pointer.forward(50)
    pointer.setheading(180)
    pointer.forward(500)
    pointer.setheading(0)


for column in range(10):
    for row in range(10):
        pointer.dot(20, random.choice(color_list))
        pointer.forward(50)
    row_shifting()

screen = Screen()
screen.exitonclick()
