


# A program to test out different matrix transformations

from turtle import Turtle as Tut, Screen
import math  # for using pi, sinus and cosinus


class Blob:

    # --- MTEHODS ----
    #   1. initialize()
    #   2. updatePos()
    #   3. scale()
    #   4. forward()
    #   5. backward()
    #   6. stepRight()
    #   7. stepLeft()
    #   8. flip()
    #   9. rotate()
    # -----------------
    def __init__(self):

                            # Initial relative coordinates according to blob
                            #  center
        self.points = [[-50,  50,     'pink'], [-40,  0,    'purple'], 
                       [-50, -50,   'orange'], [  0, 70,      'blue'], 
                       [  0, -50,    'black'], [ 50, 50,     'green'],  
                       [ 40,   0,      'red'], [ 50, -50,'lightblue']]

        self.tutsNo = 8             # Number of vertices in the blob
        self.dotsize = 1            # Size of each vertix
        self.heading = math.pi / 2  # Heading in radians 
        self.scalar = 5             # Movement step
        self.speed = 5              # Movement speed

        self.x = 0                  # Blob center
        self.y = 0

        self.tuts = [ Tut() for i in range(self.tutsNo) ]  # Array of turtles
        self.initialize()

    def initialize(self):

        for i in range(self.tutsNo):
            
            self.tuts[i].speed(0)
            self.tuts[i].penup()
            self.tuts[i].shapesize(self.dotsize)
            self.tuts[i].shape('circle')
            self.tuts[i].color(self.points[i][2]) 

        self.updatePos()

    def updatePos(self):   
                    # update position according to object center
        for i in range(self.tutsNo):
            self.tuts[i].setpos(self.points[i][0]+self.x, 
                                self.points[i][1]+self.y)

    def scale(self, scalar, multiplier=10):

        for i in range(self.tutsNo):
            self.points[i][0] *= scalar
            self.points[i][1] *= scalar

        self .updatePos()

    def forward(self):

        for i in range(self.tutsNo):
            self.x += self.scalar * math.cos(self.heading)
            self.y += self.scalar * math.sin(self.heading)

        self.updatePos()

    def backward(self):

        for i in range(self.tutsNo):
            self.x += self.scalar * math.cos(self.heading + math.pi)
            self.y += self.scalar * math.sin(self.heading + math.pi)

        self.updatePos()

    def stepRight(self):

        for i in range(self.tutsNo):
            self.x += self.scalar * math.cos(self.heading - math.pi/2)
            self.y += self.scalar * math.sin(self.heading - math.pi/2)

        self.updatePos()

    def stepLeft(self):

        for i in range(self.tutsNo):
            self.x += self.scalar * math.cos(self.heading + math.pi/2)
            self.y += self.scalar * math.sin(self.heading + math.pi/2)

        self.updatePos()

    def flip(self):

        self.heading += math.pi

        for i in range(self.tutsNo):
            self.points[i][0] *= -1
            self.points[i][1] *= -1

        self.updatePos()

    def rotate(self, direction=1, speed=0):
        # Here we have to use sinus on the y coordinates
        #  and cosinus on the x coordinates

        direction = math.pi/8*direction
        self.heading += direction

        for i in range(self.tutsNo):
            xp = self.points[i][0] 
            yp = self.points[i][1]
            r  = math.sqrt(math.pow(xp, 2) + math.pow(yp, 2))

            x_new = (xp*math.cos(direction)) - (yp*math.sin(direction))
            y_new = (xp*math.sin(direction)) + (yp*math.cos(direction))

            self.points[i][0] = x_new
            self.points[i][1] = y_new

        self.updatePos()


def run():

    screen = Screen()
    screen.delay(0)

    blob = Blob()

    screen.onkey(lambda: blob.scale(1.1), '+')
    screen.onkey(lambda: blob.scale(0.9), '-')

    screen.onkey(lambda: blob.forward(),  'Up' )
    screen.onkey(lambda: blob.backward(), 'Down')

    screen.onkey(lambda: blob.stepLeft(), 'a')
    screen.onkey(lambda: blob.stepRight(),'d')

    screen.onkey(lambda: blob.rotate( 1),   'Left')
    screen.onkey(lambda: blob.rotate(-1), 'Right')

    screen.onkey(lambda: blob.flip(), 'space')

    screen.listen()
    screen.mainloop()



if __name__ == "__main__":

    run()