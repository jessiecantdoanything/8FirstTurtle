import turtle
turtle.shape("turtle")
turtle.color("Slate Gray")


def star():
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
star()

turtle.exitonclick()