import turtle

schildkroete = turtle.Turtle()
bildschirm = schildkroete.getscreen()

schildkroete.shapesize(5,5,5)
schildkroete.shape("turtle")
schildkroete.color('red', 'yellow')
schildkroete.begin_fill()
schildkroete.forward(500)
schildkroete.left(90)
schildkroete.forward(500)
schildkroete.left(90)
schildkroete.forward(500)
schildkroete.left(90)
schildkroete.forward(1000)
schildkroete.end_fill()

turtle.done()