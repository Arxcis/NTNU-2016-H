

from turtle import Turtle, Screen
import math
import time


screen = Screen()
screen.window_height 
screen.screensize(1200, 1000)

class Star (Turtle) : 

    def __init__( self, color ):
        super().__init__()

        self.penup()
        self.speed(0)
        self.shape("circle")
        self.shapesize(2)
        self.color(color)

class Planet (Turtle) :
    
    orbitRATIO       = 1700000.0    # 1 : 1 000 000 km 
    radiusRATIO      = 12000.0      # 1 : 12000    km 

    def __init__(self, color, orbit, radius, speed):
        super().__init__()

        self.penup()
        self.speed(0)
        self.shape("circle")
        self.color(color)
                                            # Actual realworld measurements
        self.orbit          = orbit         #   Eks: 149 million kilometers
        self.radius         = radius        #   Eks:  6371 km
        self.speed          = speed         #   Eks: 108 000 km/h

                                            # Adjusted to fit to screen
        self.relativeOrbit  = self.orbit  / self.orbitRATIO
        self.relativeRadius = self.radius / self.radiusRATIO
        self.relativeSpeed = math.pi/180.0 * (speed/30000.0)

        self.rotation = 0.0
        self.x = self.relativeOrbit
        self.y = 0.0
        self.goto(self.x, self.y)
        self.shapesize(self.relativeRadius)

    def updatePosition( self ):
        self.rotation += self.relativeSpeed
        self.x = self.relativeOrbit * math.cos(self.rotation)
        self.y = self.relativeOrbit * math.sin(self.rotation)

        self.goto(self.x, self.y)

quit = False

def set_quit( ):
    global quit
    quit = True

sun     = Star  ( color="yellow" )

planets = {
    'mercury' : Planet( color="grey"  , orbit= 57910000.0, radius=2440.0,  speed=170640.0),
    'venus'   : Planet( color="green" , orbit=108200000.0, radius=6052.0,  speed=126000.0),
    'earth'   : Planet( color="blue",   orbit=149600000.0, radius=6371.0,  speed=108000.0),
    'mars'    : Planet( color="red" ,   orbit=227900000.0, radius=3390.0,  speed= 86760.0),
    'jupiter' : Planet( color="orange", orbit=778500000.0, radius=69911.0, speed= 47160.0)
}


screen.listen()

screen.onkey( set_quit , 'q' )

while not quit :


    for planet in planets:
        planets[planet].updatePosition()

screen.mainloop()


