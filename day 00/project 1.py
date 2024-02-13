from turtle import*

#we want to paint a house

#step 1 draw a square
begin_fill()
speed(30)
width(7)
color("gray")
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

forward(70)
begin_fill()
color("black")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

begin_fill()
color("yellow")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows

penup()
goto(20, 180)
pendown()
color("cyan")

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


exitonclick()
