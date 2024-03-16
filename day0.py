from turtle import *

shape("turtle")
#we want to paint house
#step
speed(30)
#step 1: draw a square
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square
#drawing a door


forward(30)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)





end_fill()
penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

left(120)
penup()
goto(200,200)
pendown()
right(90)
penup()
goto(125,125)
pendown()

begin_fill()
color("black")


forward(55)
left(90)
forward(55)
left(90)
forward(55)
left(90)
forward(55)
end_fill()

right(90)


exitonclick()