import turtle

scn = turtle.Screen()
jr = turtle.Turtle()
chris = turtle.Turtle()
gary = turtle.Turtle()
eliza = turtle.Turtle()
gary.begin_fill()


gary.speed(11)
gary.shape("turtle")
gary.color("Gold")
chris.shape("square")
chris.color("Black")
chris.speed(5)
chris.turtlesize(.5)
jr.shape("triangle")
jr.color("Rosy Brown")
jr.speed(5)
eliza.shape("circle")
eliza.color("Light Pink")
eliza.speed(5)

gary.penup()
gary.goto(0, -200)
gary.pendown()
gary.circle(200)
gary.end_fill()

chris.penup()
chris.left(40)
chris.forward(25)
chris.left(5)
chris.forward(5)
chris.pendown()

chris.forward(31)
chris.right(45)
chris.shape("circle")
chris.shapesize(4,3,1)
chris.fillcolor("black")

jr.penup()
jr.right(50)
jr.backward(40)
jr.right(5)
jr.backward(40)
jr.pendown()


jr.forward(31)
jr.left(45)
jr.shape("circle")
jr.shapesize(4,3,1)
jr.fillcolor("black")










turtle.exitonclick()