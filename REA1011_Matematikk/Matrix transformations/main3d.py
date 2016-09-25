

from turtle import Turtle as Tut, Screen
import math



def viewTransform(vec1, vec2):

    temp = Vector3(
            (vec1.x) +         0  +          0 - vec2.x,
                     0 + (vec1.y) +          0 - vec2.y,
                     0 +         0  + (vec1.z) - vec2.z )

    return temp

# --------------------------------------

class Vector3:

    def __init__(self,x,y,z):

        self.x = x
        self.y = y
        self.z = z
        self.w = 1

    def __str__(self):

        return "x: " + str(round(self.x,2))+" y: " + str(round(self.y,2))+" z: " + str(round(self.z,2))


class Camera:

    def __init__(self):
        self.center = Vector3(0,0,100.0)


camera = Camera()

# ----------------------------------------

class Cube:

    def __init__(self):

        self.vertixNo = 8
        self.matrix =[Vector3(-1,  1,  1),
                      Vector3(-1,  1, -1),
                      Vector3(-1, -1, -1),
                      Vector3(-1, -1,  1),
                      Vector3( 1,  1,  1),
                      Vector3( 1,  1, -1),
                      Vector3( 1, -1, -1),
                      Vector3( 1, -1,  1)]

        self.center = Vector3(0.0,0.0,0.0)
        self.rotation = Vector3(0,0,0)
        self.scale  = 100.0
        self.dotsize = 1
        self.color = 'green'

        self.tuts = [ Tut() for i in range(self.vertixNo) ]
        self.initialize()

        self.rotationSpeed = math.pi/20.0

    def initialize(self):

        for i in range(self.vertixNo):

            self.tuts[i].speed(0)
            self.tuts[i].penup()
            self.tuts[i].shapesize(self.dotsize)
            self.tuts[i].shape('circle')
            self.tuts[i].color(self.color)

        self.render()

    def render(self):

        # self.printMatrix()
        for i in range(self.vertixNo):

            # Local transform 
            x = self.scale * self.matrix[i].x + self.center.x
            y = self.scale * self.matrix[i].y + self.center.y
            z = self.scale * self.matrix[i].z + self.center.z

            # Camera Transform
            viewVec = viewTransform(Vector3(x,y,z), camera.center)
            print(str(viewVec))

            self.tuts[i].setpos(x, y)


    def printMatrix(self):

        print(str(self.matrix))


    # ---- Rotate transforms -----

        # Rotates the a-axis, using coordinates (b,c)
    def rotateTransform(self, alpha, a, b):

            a = (a*math.cos(alpha)) - (b*math.sin(alpha))
            b = (a*math.sin(alpha)) + (b*math.cos(alpha))

            return a, b

    def rotateZ(self, direction=1.0):
        
        direction = self.rotationSpeed * direction
        self.rotation.z += direction

        for i in range(self.vertixNo):
            self.matrix[i].x, self.matrix[i].y = self.rotateTransform(
                                                        direction, 
                                                 self.matrix[i].x,
                                                 self.matrix[i].y)
        self.render()

    def rotateX(self, direction=1.0):

        direction = self.rotationSpeed * direction
        self.rotation.x += direction

        for i in range(self.vertixNo):
            self.matrix[i].z, self.matrix[i].y = self.rotateTransform(
                                                        direction, 
                                                 self.matrix[i].z,
                                                 self.matrix[i].y)
        self.render()

    def rotateY(self, direction=1.0):

        direction = self.rotationSpeed * direction
        self.rotation.y += direction

        for i in range(self.vertixNo):
            self.matrix[i].x, self.matrix[i].z = self.rotateTransform(
                                                        direction, 
                                                 self.matrix[i].x,
                                                 self.matrix[i].z)
        self.render()

    # ----- MOVE transforms -----

    def moveX(self):
        return 0

    def moveY(self):
        return 0

    def moveZ(self):
        return 0


def main():

    screen = Screen()
    cube = Cube()

    screen.onkey(lambda: cube.rotateZ( 1.0),   'q')
    screen.onkey(lambda: cube.rotateZ(-1.0),   'w')

    screen.onkey(lambda: cube.rotateX( 1.0),    'e')
    screen.onkey(lambda: cube.rotateX(-1.0),    'r')

    screen.onkey(lambda: cube.rotateY( 1.0),    't')
    screen.onkey(lambda: cube.rotateY(-1.0),    'y')

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":

    main()










