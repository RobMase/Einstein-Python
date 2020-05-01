import turtle

schildi = turtle.Turtle()
schildi.color('red', 'yellow')

schildi.begin_fill()
while True:
    schildi.forward(200)
    schildi.left(170)
    if abs(schildi.pos()) < 1:
        break
schildi.end_fill()
turtle.done()