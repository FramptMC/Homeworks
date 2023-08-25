from turtle import *
speed(30)
width(10)
color("pink") #epic barbie girl moment
forward(250)
left(90)

forward(250)
left(90)

forward(250)
left(90)

forward(250)
left(90)

#door
forward(100)
left(90)
color("green")
begin_fill()
forward(100)
right(90)

forward(50)
right(90)

forward(100)
end_fill()
#epic roof
penup()
goto(250,250)
pendown()
color("brown")

begin_fill()
right(150)
forward(250)

left(120)
forward(250)
end_fill()

#windows (not IOS u dummy) /left
penup()
goto(90,140)
pendown()
color("blue")
begin_fill()
right(60)
forward(30)

right(90)
forward(60)

right(90)
forward(30)

right(90)
forward(60)
end_fill()

#windows (not IOS u dummy) /right
penup()
goto(160,140)
pendown()
color("blue")
begin_fill()
left(90)
forward(30)

left(90)
forward(60)

left(90)
forward(30)

left(90)
forward(60)

end_fill()


exitonclick()