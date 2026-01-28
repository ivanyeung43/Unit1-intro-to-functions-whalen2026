import turtle
from turtle import *
t = Turtle()
t.shape('turtle')



def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(90)
turtle.done()
