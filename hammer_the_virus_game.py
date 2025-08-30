#download Hammer and virus files
import turtle
import time
import os
import random

v = turtle.Turtle()
h= turtle.Turtle()
s = turtle.Screen()
points = 0

#screen

s.setup(700,600)
s.bgcolor ('#28282B')
s.title("Hammer The Virus")
s.addshape('hammer.gif')
s.addshape('virus.gif')

#virus

v.shape("virus.gif")
v.penup()
v.goto(0,0)

#hammer
h.ht()
h.shape("hammer.gif")
h.penup()

p = turtle.Turtle()
p.hideturtle()
p.penup()
p.goto(-50,260)
p.write(f"Score = {points} ", font= ("verdana",20,"bold"))


def score():
    global points
    p.clear()
    points += 1
    p.color("Red")
    p.write(f"Score = {points} ", font= ("verdana",20,"bold"))
    p.color("Yellow")
    time.sleep(0.2)
    print(points)

    p.write(f"Score = {points} ", font= ("verdana",20,"bold"))


def checker(x,y):
    h.goto(x+20,y-10)
    h.showturtle()
    time.sleep(0.1)
    h.ht()
    if x > v.xcor()-20 and x < v.xcor()+20 and y > v.ycor()-20 and y < v.ycor()+20:
        score()

s.listen()
s.onscreenclick(checker,1)

while True:
    v.ht()
    x= random.randint(-315,315)
    y= random.randint(-265,265)
    v.goto(x,y)
    v.showturtle()
    time.sleep(0.99999999999999)


s.mainloop()

turtle.done()
