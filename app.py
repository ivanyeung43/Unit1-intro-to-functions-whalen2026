import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
sidelength = 100
rotate = 90
def square(sidelength,rotate):
    for i in range(4):
        t.forward(sidelength)
        t.left(rotate)

def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, rotate)
        length += 5
        t.right(5)
addSquares(60)




turtle.done()
