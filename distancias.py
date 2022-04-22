from turtle import *
radius = 1
speed(0)
x1 = float(input("x1:"))
y1 = float(input("y1:"))

x2 = float(input("x2:"))
y2 = float(input("y1:"))

forward(150)
stamp()
backward(150)
left(90)
forward(150)
stamp()

penup()
color("blue")
goto(x1,y1)
pendown()
circle(radius)

color("orange")
goto(x2,y2)
color("blue")
circle(radius)

print("distance is:", (((x2-x1)**2+ (y2-y1)**2))**0.5)
style = ('Courier', 10, 'italic')
write((((x2-x1)**2+ (y2-y1)**2))**0.5, font = style)
