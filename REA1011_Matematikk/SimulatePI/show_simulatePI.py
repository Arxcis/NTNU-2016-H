
from turtle import Turtle, Screen
import random
import math

import gc

# Turtle is sort of a pen which you move around
# to draw stuff on the screen. Here we init
# two turtles. One to draw red dots,
# and one to draw blue dots.
# Also we init the screen/window-object.

tut1 = Turtle()
tut2 = Turtle()
screen = Screen()

# Set turtle attributes
screen.delay(0)

# tut1 init
tut1.penup()
tut1.color('red')
tut1.speed(0)
tut1.goto(-100,0)
tut1.left(90)
tut1.shape('circle')
tut1.shapesize(0.05)


# tut2 init
tut2.penup()
tut2.color('blue')
tut2.speed(0)
tut2.goto(100,0)
tut2.left(90)
tut2.shape('circle')
tut2.shapesize(0.05)

# Global variables

# CONSTANTS
circle_x = 1
circle_y = 1
rect_height = 2
rect_width = 2

rand_x = 0
rand_y = 0

just_x = '?'
just_y = '?'

total_hits = 0
circle_hits = 0

while(total_hits < 10000000000):

    # Random.random() returns a value between 0 and < 1
    #  Which means that rand_x will get a value between
    #  0 and 2.
    rand_x = rect_height * random.random()
    rand_y = rect_width * random.random()

    just_x = circle_x - rand_x
    just_y = circle_y - rand_y

    if (just_x*just_x)+(just_y*just_y) <= 1: 

        #if total_hits % 100 == 0:
        #   tut1.goto((rand_x*200)-200, (rand_y*200)-150)
        #  tut1.stamp()
        circle_hits += 1

    #else:
        #if total_hits % 100 == 0: 
            #  tut2.goto((rand_x*200)-200, (rand_y*200)-150)
            # tut2.stamp()

    total_hits += 1

    if total_hits % 10000 == 0:
      #  gc.collect()
        print("Hits %d of 10 000 000 000: PI = %.6f xm^2" % (total_hits, 4 * (circle_hits/total_hits)))





# The mainloop opens a window which refreshes 
# like a update-loop.
screen.mainloop()



"""
class Turtle:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = 'black' 

    def goto(self, newx, newy):

        return 0

"""









