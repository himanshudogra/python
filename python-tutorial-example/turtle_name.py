import turtle 
import random

turtle.bgcolor('black') 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 

t = turtle.Pen()



def line(x1,y1,x2,y2,color,pensize):
    t.penup()
    t.pensize(pensize)
    t.color(color)
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)
    t.penup()
while True:
    line(-200,30,-200,-30,random.choice(colors),3)
    line(-200,0,-150,0,random.choice(colors),3)
    line(-150,30,-150,-30,random.choice(colors),3)
    line(-100,30,-100,-30,random.choice(colors),3)
    line(-125,30,-75,30,random.choice(colors),3)
    line(-125,-30,-75,-30,random.choice(colors),3)
    line(-50,30,-50,-30,random.choice(colors),3)
    line(-50,30,-25,0,random.choice(colors),3)
    line(-25,0,0,30,random.choice(colors),3)
    line(0,30,0,-30,random.choice(colors),3)
    line(50,30,25,-30,random.choice(colors),3)
    line(50,30,75,-30,random.choice(colors),3)
    line(40,0,60,0,random.choice(colors),3)
    line(100,30,100,-30,random.choice(colors),3)
    line(100,30,140,-30,random.choice(colors),3)
    line(140,-30,140,30,random.choice(colors),3)
    line(200,30,170,30,random.choice(colors),3)
    line(170,30,170,0,random.choice(colors),3)
    line(170,0,200,0,random.choice(colors),3)
    line(200,0,200,-30,random.choice(colors),3)
    line(200,-30,170,-30,random.choice(colors),3)
    line(225,30,225,-30,random.choice(colors),3)
    line(225,0,260,0,random.choice(colors),3)
    line(260,30,260,-30,random.choice(colors),3)
    line(285,30,285,-30,random.choice(colors),3)
    line(285,-30,325,-30,random.choice(colors),3)
    line(325,30,325,-30,random.choice(colors),3)

