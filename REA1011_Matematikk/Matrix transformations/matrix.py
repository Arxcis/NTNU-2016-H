
import copy
import math
from turtle import Turtle, Screen


# ----------------- Vectors ---------------------

class Vector4:
    def __init__(self,x,y,z,w):

        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return '['+str(self.x)+','+str(self.y)+','+str(self.z)+','+str(self.w)+']'


class Vector3:
    def __init__(self, x,y,z):

        self.x = x
        self.y = y
        self.z = z


# ---------------------- MATRIX class --------------------------

class Matrix4:

    identityMatrix = [[1.0, 0.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, 0.0],
                      [0.0, 0.0, 1.0, 0.0],
                      [0.0, 0.0, 0.0, 1.0]]

    def __init__(self):
        return None

    def translate( self, vec3 ):
 
        output = copy.deepcopy(self.identityMatrix)

        output[0][3] = vec3.x
        output[1][3] = vec3.y
        output[2][3] = vec3.z

        return output

    def scaler (self, vec3):

        output = copy.deepcopy(self.identityMatrix)

        output[0][0] = vec3.x
        output[1][1] = vec3.y
        output[2][2] = vec3.z

        return output

    def rotate_Z (self, z):

        output = copy.deepcopy(self.identityMatrix)

        output[0][0] =  math.cos(z)
        output[0][1] =  -math.sin(z)
        output[1][0] =  math.sin(z)
        output[1][1] =  math.cos(z)

        return output

    def rotate_Y (self, y):

        output = copy.deepcopy(self.identityMatrix)

        output[0][0] =  math.cos(y)
        output[0][2] =  math.sin(y)
        output[2][0] =  -math.sin(y)
        output[2][2] =  math.cos(y)

        return output

    def rotate_X (self, x):

        output = copy.deepcopy(self.identityMatrix)

        output[1][1] =  math.cos(x)
        output[1][2] =  -math.sin(x)
        output[2][1] =  math.sin(x)
        output[2][2] =  math.cos(x)

        return output

    def projection (self):

        near = .004
        far  = 100.0

        output = copy.deepcopy(self.identityMatrix)

        output[2][2] = (-far/(far-near))
        output[2][3] =  -1
        output[3][2] = (-far*near/(far-near))
        output[3][3] = 0

        return output


# --------------------- ORPHAN MATRIX method --------------------------

def vector_dot_matrix(vec4, mat):

    output = [ mat[0][0]*vec4.x + mat[0][1]*vec4.y + mat[0][2]*vec4.z + mat[0][3]*vec4.w,
               mat[1][0]*vec4.x + mat[1][1]*vec4.y + mat[1][2]*vec4.z + mat[1][3]*vec4.w,
               mat[2][0]*vec4.x + mat[2][1]*vec4.y + mat[2][2]*vec4.z + mat[2][3]*vec4.w,
               mat[3][0]*vec4.x + mat[3][1]*vec4.y + mat[3][2]*vec4.z + mat[3][3]*vec4.w ]

    return Vector4( output[0], output[1], output[2], output[3] )  # Vec4


# ------------------------- Cube class ----------------------------

class Cube:

    camera = Vector4 (0.0,0.0,-150.0,1.0)

    def __init__(self, vec4):

        self.position      = vec4
        self.rotation      = Vector4 ( 0.0, 0.0, 0.0, 1.0 )

        self.speed  = Vector3 ( 0,0,0 )
        self.rspeed = Vector3 ( 0,0,0 )
        self.scale  = Vector3 ( 20.0, 20.0, 20.0 )

        self.no_points = 8

        self.points = [ Vector4(  1,  1,  1, 1),
                        Vector4(  1,  1, -1, 1),
                        Vector4(  1, -1,  1, 1),
                        Vector4(  1, -1, -1, 1),
                        Vector4( -1,  1,  1, 1),
                        Vector4( -1,  1, -1, 1),
                        Vector4( -1, -1,  1, 1),
                        Vector4( -1, -1, -1, 1)]

        self.turtle = [Turtle() for i in range(self.no_points)]
        self.init_tuts()
 
        self.init_matrixes()
        print(self.position)


    def init_tuts (self):

        for i in range (self.no_points):
            self.turtle[i].penup()
            self.turtle[i].speed(0)
            self.turtle[i].shape('circle')

    def init_matrixes (self):
                # Initializing matrixes
        self.speed_mat      = Matrix4().translate  (self.speed )
        self.rspeed_mat     = Matrix4().translate  (self.rspeed )
        self.scaling_mat    = Matrix4().scaler     (self.scale)
        self.rotate_Z       = Matrix4().rotate_Z   (self.rotation.z)
        self.rotate_Y       = Matrix4().rotate_Y   (self.rotation.y)
        self.rotate_X       = Matrix4().rotate_X   (self.rotation.x)
        self.cube_trans     = Matrix4().translate  (self.position)
        self.camera_trans   = Matrix4().translate  (self.cameraDelta(self.camera))
        self.projection_mat = Matrix4().projection ()

    def update(self):

        self.init_matrixes()

                # Update cube
        self.position = vector_dot_matrix(self.position, self.speed_mat)
        self.rotation = vector_dot_matrix(self.rotation, self.rspeed_mat)

                # Update cube points    
        for i in range(self.no_points):
            temp = self.points[i]
            temp = vector_dot_matrix(temp, self.scaling_mat)
            temp = vector_dot_matrix(temp, self.rotate_Z)
            temp = vector_dot_matrix(temp, self.rotate_Y)
            temp = vector_dot_matrix(temp, self.rotate_X)
            temp = vector_dot_matrix(temp, self.cube_trans)
            temp = vector_dot_matrix(temp, self.camera_trans)
            #temp = vector_dot_matrix(temp, self.projection_mat)

                # Normalize
            #print(temp)
            #temp = Vector3(temp.x/temp.w, temp.y/temp.w, temp.z/temp.w)

            self.turtle[i].goto(temp.x, temp.y)

    def cameraDelta(self, camera):
        output = Vector4(self.position.x - camera.x,
                         self.position.y - camera.y,
                         self.position.z - camera.z,
                         1.0)
        return output

# --------------- GLOBALS ------------------

screen = Screen()
cube = Cube( Vector4( 0.0, 0.0, 0.0, 1.0))
quit = False


# ---------------- INPUT --------------------------

def right ():
    cube.speed.x += 1.0
    print(cube.speed.x, cube.speed.y, cube.speed.z)     

def left ():
    cube.speed.x -= 1.0
    print(cube.speed.x, cube.speed.y, cube.speed.z) 

def up   ():
    cube.speed.y += 1.0
    print(cube.speed.x, cube.speed.y, cube.speed.z) 

def down ():
    cube.speed.y -= 1.0
    print(cube.speed.x, cube.speed.y, cube.speed.z) 

def w ():
    cube.rspeed.z += 0.05
    print(cube.rspeed.x, cube.rspeed.y, cube.rspeed.z) 

def s ():
    cube.rspeed.z -= 0.05
    print(cube.rspeed.x, cube.rspeed.y, cube.rspeed.z)

def d ():
    cube.rspeed.y += 0.05
    print(cube.rspeed.x, cube.rspeed.y, cube.rspeed.z)

def a ():
    cube.rspeed.y -= 0.05
    print(cube.rspeed.x, cube.rspeed.y, cube.rspeed.z)

def e ():
    cube.rspeed.x += 0.05
    print(cube.rspeed.x, cube.rspeed.y, cube.rspeed.z)

def q ():
    cube.rspeed.x -= 0.1
    print(cube.rspeed.x, cube.rspeed.y, cube.rspeed.z)


def pluss():
    cube.scale.x += 10
    cube.scale.y += 10
    cube.scale.z += 10

def minus():
    cube.scale.x -= 10
    cube.scale.y -= 10
    cube.scale.z -= 10

def space():
    cube.position.z += 1.0
    print(cube.position.x, cube.position.y, cube.position.z )
    print(cube.speed.x, cube.speed.y, cube.speed.z)

def c ():
    cube.position.z -= 1.0
    print(cube.position.x, cube.position.y, cube.position.z )
    print(cube.speed.x, cube.speed.y, cube.speed.z) 

def x ():
    global quit
    quit = True

screen.onkey( right,  'Right')
screen.onkey( left,   'Left')
screen.onkey( up,     'Up')
screen.onkey( down, 'Down')

screen.onkey( w, 'w')
screen.onkey( s, 's')
screen.onkey( d, 'd')
screen.onkey( a, 'a')
screen.onkey( e, 'e')
screen.onkey( q, 'q')

screen.onkey( minus, '-')
screen.onkey( pluss, '+')

screen.onkey( space, 'space')
screen.onkey( c    , 'c')
screen.onkey( x    , 'x')


if __name__ == "__main__":

    while not quit:

        screen.listen()
        cube.update()


    screen.mainloop()

