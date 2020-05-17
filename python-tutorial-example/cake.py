import turtle
import random

# set the background color for the page
bg = turtle.Screen()
bg.bgcolor("black")

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed()

def line(x1, y1, x2, y2, color, pensize):
  tommy.penup()
  tommy.goto(x1, y1)
  tommy.color(color)
  tommy.pensize(pensize)
  tommy.pendown()
  tommy.goto(x2, y2)
  tommy.penup()
  
snow_colors = ["pink", "blue", "gold", "light yellow", "light blue",  "purple", "grey", "magenta", 'green', 'orange', 'gold', 'red', 'red']

line(-190, -180, 190, -180, random.choice(snow_colors), 8)
line(-160, -150, 160, -150, random.choice(snow_colors), 8)
line(-130, -120, 130, -120, random.choice(snow_colors), 8)

# draw cake
tommy.goto(-70,-110)
tommy.begin_fill()
tommy.pendown()
tommy.color("pink")
tommy.goto(50,-110)
tommy.left(90)
tommy.forward(60)
tommy.left(90)
tommy.forward(125)
tommy.left(90)
tommy.forward(60)
tommy.penup()
tommy.end_fill()

#draw candles

def candle(x, color):
  tommy.goto(x, -40)
  tommy.color(color)
  tommy.pendown()
  tommy.pensize(3)
  tommy.goto(x, -20)
  tommy.penup()

candle(-65, random.choice(snow_colors))
candle(-50, random.choice(snow_colors))
candle(-30, random.choice(snow_colors))
candle(-10, random.choice(snow_colors))
candle(0, random.choice(snow_colors))
candle(10, random.choice(snow_colors))
candle(30, random.choice(snow_colors))
candle(50, random.choice(snow_colors))
#candle(60, random.choice(snow_colors))

# print message
tommy.goto(-250, 50)
tommy.color('orange')
tommy.pendown()
#tommy.write("Happy Birthday!",None,None, "20pt bold")
tommy.write("!JBS!  Wish you a very Happy Birthday in advcance!!",move=False, font=("Arial", 20, "bold"))
    


# send the turtle to the corner
tommy.penup()
while True:
    tommy.goto(-500, 30)
    tommy.color('white')
