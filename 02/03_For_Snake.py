import turtle

schildi = turtle.Turtle()

schildi.shapesize(1,1,1)
schildi.shape("turtle") # “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
schildi.speed(3) # 1 - 10 (0)

for index in range(4):
    schildi.forward(200)
    schildi.left(90) # in grad (0 - 360)
else:
    schildi.dot(50)

# schildi.setpos(-300, 0)
# for index in range(8):
#     schildi.left(45)
#     schildi.forward(200)

turtle.done()