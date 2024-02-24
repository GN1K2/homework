from turtle import *


#we want to make first house

#step 1: draw a square
speed(30)
begin_fill()
width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square


#drawing a door

begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()         #going to roof
goto(200,200)
pendown()

color("blue")   #drawing roof
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows

penup()
goto(20, 180)
pendown()
color("black")

begin_fill()
left(120)
forward(50)
right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

penup()
goto(180, 180)
pendown()

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)
end_fill()

penup()

goto(300,0)
right(90)


begin_fill()
width(7)
color("orange")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square


#drawing a door

begin_fill()
forward(70)
color("purple")
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()         #going to roof
goto(500,200)
pendown()

color("green")   #drawing roof
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows

penup()
goto(20, 180)
pendown()
color("black")

begin_fill()
left(120)
forward(50)
right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

penup()
goto(370, 180)
pendown()

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)
end_fill()

penup()

goto(430,180)
begin_fill()
right(90)
pendown()

forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)
end_fill()


penup()
goto(-300,0)
pendown()

begin_fill()
width(7)
color("orange")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

begin_fill()
forward(70)
color("red")
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()         #going to roof
goto(-100,200)
pendown()


color("grey")   #drawing roof
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()






exitonclick()