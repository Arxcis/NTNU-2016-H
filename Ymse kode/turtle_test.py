
"""
  Filename    : turtle_test.py
  Author      : Jonas Solsvik
  Created     : 30.08.16

  Description :  A Small turtle graphics program.
                  This script will be used for tutorial purposes
                   It is beiing used in the first lecture of Jonas
                    "Turtle-graphics totorials" - series". '        
"""

from turtle import Turtle, Screen

# Initialize turtle objects.
fred = Turtle()
paul = Turtle()
screen = Screen()

# Init attributes
fred.color('red')
paul.color('green')
fred.penup()
paul.penup()
fred.shapesize(3)
paul.shapesize(3)
fred.speed(3)
paul.speed(3)

# Move around
fred.forward(50)
paul.backward(50)

fred.left(90)
paul.left(90)


while 1:

    fred.forward(50)
    fred.right(90)

    paul.forward(50)
    paul.left(90)


screen.mainloop()

"""
tut.color()
tut.penup()
tut.pendown()
tut.shapesize()
tut.forward()
tut.backward()
tut.left()
tut.right()
"""
