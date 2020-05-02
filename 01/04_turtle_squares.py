
from turtle import *
import random

screen = Screen()
schildi = Turtle()
schildi.speed(0)

colormode(255)
count = random.randrange(100, 500)
maxsize = 100
minsize = 20

for i in range(0, count):
    schildi.penup()
    schildi.setpos(random.randrange(0, screen.canvwidth), random.randrange(0, screen.canvheight))
    schildi.pendown()
    col = (random.randrange(100, 255), random.randrange(40, 150), random.randrange(0, 30))
    schildi.color(col, col)
    schildi.begin_fill()
    size = random.randrange(minsize, int(minsize + 1 + ((maxsize - minsize)*((count - i) / count))))
    schildi.left(random.randrange(0, 360))
    schildi.forward(size)
    schildi.left(90)
    schildi.forward(size)
    schildi.left(90)
    schildi.forward(size)
    schildi.left(90)
    schildi.forward(size)
    schildi.end_fill()
    schildi.penup()
