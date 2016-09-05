

from turtle import Turtle, Screen
import random as r
import math

print(r.random())


# Init objects
tut = Turtle()
screen = Screen()

# Init window
screen.screensize(1500, 1000)

# Init tut
tut.speed(0)
tut.penup()
tut.color('red')
tut.shape('circle')
tut.shapesize(.1)

# CONST
length = 6
height = 2
area = length * height
centers = [[1+(1*x),1] for x in range(5)]
print(centers)
formula = 'x^2 + y^2 = 1'


# VAR
precision = 0
randlen = 0
randhi = 0
plot = False

hits = 0

while precision < 15000:

    randlen = length * r.random()
    randhi = height * r.random()

    for center in centers:

        x = center[0]
        y = center[1]

        x_diff = x - randlen
        y_diff = y - randhi

        if math.pow(x_diff,2) + math.pow(y_diff,2) <= 1:
            tut.color('red')
            tut.goto((150*randlen)-400, (150*randhi-200))
            tut.stamp()

            hits += 1
            break

    else:
        tut.color('blue')
        tut.goto((150*randlen)-400, (150*randhi-200))
        tut.stamp()


    precision +=1
    if precision % 10 == 0:
        print("Approx area: %2f" % (area*(hits/precision)))
 
    plot = False




screen.mainloop()




