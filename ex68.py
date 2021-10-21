#ex68
from turtle import *

def triangle(n):
    begin_fill()
    down()
    for i in range(2):
        forward(n)
        left(120)
    end_fill()
    begin_fill()
    forward(n*2)
    left(120)
    for i in range(2):
        forward(n)
        left(120)
    end_fill()
    begin_fill()
    forward(n)
    left(120)
    forward(n*2)
    left(120)
    for i in range(2):
        forward(n)
        left(120)
    end_fill()


def sapin(n):
    begin_fill()
    down()
    forward(n)
    left(120)
    forward(n*2)
    left(120)
    forward(n*2)
    left(120)
    forward(n)
    left(90)
    forward(20)
    
    end_fill()
   

    
    



