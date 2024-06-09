# Write your code here :-)
from turtle import *

shape('turtle')
shapesize(2)
bgcolor('darkblue')
color('yellow')
speed(0)

def polylines(sides, length, angle):
    for i in range(sides):
        forward(length)
        right(angle)

def spiral(sides, length, angle):
    for i in range(sides):
        forward(length)
        right(angle)
        length = length + 3

spiral(363, 20, 124)
