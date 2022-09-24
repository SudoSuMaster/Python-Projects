from turtle import *
from random import *
import turtle
import time



#SCREEN SETUP
setup(800, 500)
title("Turtle race")
turtle.bgcolor("forestgreen")
speed(0)

# HEADING
penup() #LINE DELETE
goto(-100, 205)
color("white")
write("TURTLE RACE", font=("Arial", 20, "bold"))


# DIRT
goto(240, 200)
pendown()
color("chocolate")
begin_fill()
for i in range (1):
    right(90)
    forward(400)
    left(90)
    forward(20)
    left(90)
    forward(400)


end_fill()





# TURTLE 1
turtle.speed(50)

blue_turtle = Turtle()
blue_turtle.color("cyan")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5)
blue_turtle.penup()
blue_turtle.goto(-300, 150)
blue_turtle.pendown()

# TURTLE 2
pink_turtle = Turtle()
pink_turtle.color("magenta")
pink_turtle.shape("turtle")
pink_turtle.shapesize(1.5)
pink_turtle.penup()
pink_turtle.goto(-300, 50)
pink_turtle.pendown()

# TURTLE 3
yellow_turtle = Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(1.5)
yellow_turtle.penup()
yellow_turtle.goto(-300, -50)
yellow_turtle.pendown()

# TURTLE 4
red_turtle = Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.shapesize(1.5)
red_turtle.penup()
red_turtle.goto(-300, -150)
red_turtle.pendown()


 
# taking input
name = turtle.textinput("Wie gaat er winnen ?", "Name")
 
# print name input



while blue_turtle.xcor() <= 230 and pink_turtle.xcor() <= 230 and yellow_turtle.xcor() <= 230 and red_turtle.xcor() <= 230:
    blue_turtle.forward(randint(1, 3))
    pink_turtle .forward(randint(1, 3))
    yellow_turtle.forward(randint(1, 3))
    red_turtle.forward(randint(1, 3))




#WIN 

if blue_turtle.xcor() > pink_turtle.xcor() and blue_turtle.xcor() > yellow_turtle.xcor() and blue_turtle.xcor() > red_turtle.xcor():
    print("Blue turtle wins!", "Uw gekozen turtle was", name)
    for i in range(72):
        blue_turtle.right(5)
        blue_turtle.shapesize(2.5)


elif pink_turtle.xcor() > blue_turtle.xcor() and pink_turtle.xcor() > yellow_turtle.xcor() and pink_turtle.xcor() > red_turtle.xcor():
    print("pink turtle wins!", "Uw gekozen turtle was", name)
    for i in range(72):
        pink_turtle.right(5)
        pink_turtle.shapesize(2.5)

elif yellow_turtle.xcor() > blue_turtle.xcor() and yellow_turtle.xcor() > pink_turtle.xcor() and yellow_turtle.xcor() > red_turtle.xcor():
    print("Yellow turtle wins!", "Uw gekozen turtle was", name)
    for i in range(72):
        yellow_turtle.right(5)
        yellow_turtle.shapesize(2.5)

else: 
    print("Red turtle wins!", "Uw gekozen turtle was", name)
    for i in range(72):
        red_turtle.right(5)
        red_turtle.shapesize(2.5)


turtle.done()
