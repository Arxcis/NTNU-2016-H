
# simulate PI


from turtle import Turtle, Screen
import random
import math


# Init tut and screen 
tut = Turtle()
tut1 = Turtle()
screen = Screen()

# Set tut attrs
tut.speed(0)
tut.shape('circle')
tut.color('red')
tut.shapesize(.1)
tut.penup()

tut1.speed(0)
tut1.shape('circle')
tut1.color('blue')
tut1.shapesize(.1)
tut1.penup()

# Screen
screen.delay(0)

# Vars
precision = 0
hits = 0

x = 1.0
y = 1.0
area = 4

while precision < 150000000:

    xr = (x+x) * random.random()
    yr = (y+y) * random.random()

    xd = x - xr
    yd = y - yr

    if math.pow(xd, 2) + math.pow(yd, 2) <= 1:

        #tut.goto((xr*200)-200, (yr*200)-200)
        #tut.stamp()
        hits += 1

    
        #tut1.goto((xr*200)-200, (yr*200)-200)
        #tut1.stamp()

    precision += 1

    if precision % 1000 == 0:
        print("Approx area: %10f" % (4*(hits/precision)))

#screen.mainloop()