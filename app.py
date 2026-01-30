import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(10)
sidelength = 100
rotate = 144
def square(sidelength,rotate):
    for i in range(5):
        t.forward(sidelength)
        t.left(rotate)

def addSquares(iRange):
    length = 20
    for i in range(iRange):
        square(length, rotate)
        length += 5
        t.right(10)
addSquares(120)




turtle.done()
