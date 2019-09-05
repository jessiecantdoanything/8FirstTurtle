import turtle
turtle.shape("turtle")
turtle.color("thistle")
turtle.speed(.5)
def square():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

for i in range(55):
    square()
    turtle.right(5)


turtle.exitonclick()

