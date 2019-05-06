# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:54:26 2019

@author: progs
"""

import turtle

import time

import random

#screen

a = turtle.Screen()

a.setup(600,600)

a.bgcolor('orange')

a.title('DODGE')

# cannon 1

can1 = turtle.Turtle()

can1.hideturtle()

can1.color('crimson')

can1.shape('square')

can1.shapesize(2,18)

can1.penup()

can1.right(60)

can1.goto(-325,325)

can1.showturtle()

#cannon 1 head

ch1 = turtle.Turtle()

ch1.hideturtle()

ch1.color('light blue')

ch1.shape('circle')

ch1.shapesize(2,4)

ch1.penup()

ch1.goto(-240,170)

ch1.showturtle()

# cannon 2

can2 = turtle.Turtle()

can2.hideturtle()

can2.color('crimson')

can2.shape('square')

can2.shapesize(2,18)

can2.penup()

can2.left(60)

can2.goto(325,325)

can2.showturtle()

#cannon 2 head

ch2 = turtle.Turtle()

ch2.hideturtle()

ch2.color('light blue')

ch2.shape('circle')

ch2.shapesize(2,4)

ch2.penup()

ch2.goto(240,170)

ch2.showturtle()

# deffender

b = turtle.Turtle()

b.left(90)

b.color('green')

b.shapesize(2,2)

b.penup()

b.goto(0,-250)

def up():

    b.forward(50)

    b.speed(0)

    

def left():

    b.left(90)

    b.speed(0)

def right():

    b.right(90)

    b.speed(0)

def down():

    b.backward(50)

    b.speed(0)

# pen

s = turtle.Turtle()

s.hideturtle()

s.color('white')

s.pensize(10)

s.penup()

s.goto(0,220)

s.pendown()

# bullet cannon 1

b1 = turtle.Turtle()

b1.hideturtle()

b1.shape('triangle')

b1.shapesize(1,1,1)

b1.penup()

b1.goto(-240,170)

b1.color('dark red')

b1.right(60)

# bullet cannon 1 2

b11 = turtle.Turtle()

b11.hideturtle()

b11.shape('triangle')

b11.shapesize(1,1,1)

b11.penup()

b11.goto(-240,170)

b11.color('dark red')

b11.right(60)

# bullet cannon 1 3

b12 = turtle.Turtle()

b12.hideturtle()

b12.shape('triangle')

b12.shapesize(1,1,1)

b12.penup()

b12.goto(-240,170)

b12.color('dark red')

b12.right(60)

# bullet cannon 2

b2 = turtle.Turtle()

b2.hideturtle()

b2.shape('triangle')

b2.shapesize(1,1,1)

b2.penup()

b2.goto(240,170)

b2.color('dark red')

b2.left(60)

# bullet cannon 2 2

b22 = turtle.Turtle()

b22.hideturtle()

b22.shape('triangle')

b22.shapesize(1,1,1)

b22.penup()

b22.goto(240,170)

b22.color('dark red')

b22.left(60)

# bullet cannon 2 3

b23 = turtle.Turtle()

b23.hideturtle()

b23.shape('triangle')

b23.shapesize(1,1,1)

b23.penup()

b23.goto(240,170)

b23.color('dark red')

b23.left(60)

#line boundary

l = turtle.Turtle()

l.color('white')

l.pensize(15)

l.hideturtle()

l.forward(290)

l.backward(580)

l.right(90)

l.forward(290)

l.left(90)

l.forward(580)

l.left(90)

l.forward(290)

#score board

s2 = turtle.Turtle()

s2.hideturtle()

s2.color('white')

s2.pensize(15)

# fuctions

a.listen()

a.onkeypress(up , 'w')

a.onkeypress(left , 'a')

a.onkeypress(right , 'd')

a.onkeypress(down , 's')

#score variable

score = 0

def collid():

    if b.xcor() == b1.xcor() and b.ycor() == b1.ycor() or b1.xcor() > b.xcor()-20 and b1.xcor() < b.xcor() +20 and (b1.ycor() < b.ycor() + 20) and b1.ycor() > b.ycor() - 20:

        s.write('GAME OVER' , align = 'center' , font = ('courier' , 24 , 'underline'))

        time.sleep(3)

        turtle.bye()

def collid1():

    if b.xcor() == b11.xcor() and b.ycor() == b11.ycor() or b11.xcor() > b.xcor()-20 and b11.xcor() < b.xcor() +20 and (b11.ycor() < b.ycor() + 20) and b11.ycor() > b.ycor() - 20:

        s.write('GAME OVER' , align = 'center' , font = ('courier' , 24 , 'underline'))

        time.sleep(3)

        turtle.bye()

def collid2():

    if b.xcor() == b12.xcor() and b.ycor() == b12.ycor() or b12.xcor() > b.xcor()-20 and b12.xcor() < b.xcor() +20 and (b12.ycor() < b.ycor() + 20) and b12.ycor() > b.ycor() - 20:

        s.write('GAME OVER' , align = 'center' , font = ('courier' , 24 , 'underline'))

        time.sleep(3)

        turtle.bye()

def collide():

    if b.xcor() == b2.xcor() and b.ycor() == b2.ycor() or b2.xcor() > b.xcor()-10 and b2.xcor() < b.xcor() +10 and (b2.ycor() < b.ycor() + 20) and b2.ycor() > b.ycor() - 20:

        s.write('GAME OVER' , align = 'center' , font = ('courier' , 24 , 'underline'))

        time.sleep(3)

        turtle.bye()

def collide1():
    if b.xcor() == b22.xcor() and b.ycor() == b22.ycor() or b22.xcor() > b.xcor()-10 and b22.xcor() < b.xcor() +10 and (b22.ycor() < b.ycor() + 20) and b22.ycor() > b.ycor() - 20:

        s.write('GAME OVER' , align = 'center' , font = ('courier' , 24 , 'underline'))

        time.sleep(3)

        turtle.bye()

def collide2():

    if b.xcor() == b23.xcor() and b.ycor() == b23.ycor() or b23.xcor() > b.xcor()-10 and b23.xcor() < b.xcor() +10 and (b23.ycor() < b.ycor() + 20) and b23.ycor() > b.ycor() - 20:

        s.write('GAME OVER' , align = 'center' , font = ('courier' , 24 , 'underline'))

        time.sleep(3)

        turtle.bye()

# boundary restriction

def boundaryup():

    if b.xcor() >= -300 and b.ycor() >= -10:

        s.write('GAME OVER' , align = 'center' , font = ('courier' , 24 , 'underline'))

        time.sleep(3)

        turtle.bye()

def boundarylt():

    if b.xcor() <= -290 or b.ycor() <= -290:

        s.write('GAME OVER' , align = 'center' , font = ('courier' , 24 , 'underline'))

        time.sleep(3)

        turtle.bye()

def boundaryrt():

    if b.xcor() >= 300 or b.ycor() <= -290:

        s.write('GAME OVER' , align = 'center' , font = ('courier' , 24 , 'underline'))

        time.sleep(3)

        turtle.bye()

def boundarydwn():

    if b.ycor() <= -290:

        s.write('GAME OVER' , align = 'center' , font = ('courier' , 24 , 'underline'))

        time.sleep(3)

        turtle.bye()

def move():

    if c6 >= 3:

        b.forward(20)

        time.sleep(0.5)

        b.forward(20)

# misc

c6 = time.perf_counter()    

# main loop

while True:

    move()

    b1.speed(5)

    b11.speed(5)

    b12.speed(5)

    b2.speed(5)

    b22.speed(5)

    b23.speed(5)

              

    x = random.randint(-280,280)

    y = random.randint(-280,-10)

    x2 = random.randint(-280,280)

    y2 = random.randint(-280,-10)

    x3 = random.randint(-280,280)

    y3 = random.randint(-280,-10)

    x1 = random.randint(-280,280)

    y1 = random.randint(-280,-10)

    x11 = random.randint(-280,280)

    y11 = random.randint(-280,-10)

    x12 = random.randint(-280,280)

    y12 = random.randint(-280,-10)

    #showturtle

    b1.showturtle()

    b2.showturtle()

    b11.showturtle()

    b22.showturtle()

    b12.showturtle()

    b23.showturtle()

    #goto

    b1.goto(x,y)

    boundaryup()

    boundarylt()

    boundaryrt()

    boundarydwn()

    collide()

    collid()

    collid1()

    collide1()

    collid2()

    collide2()

    b2.goto(x1,y1)

    boundaryup()

    boundarylt()

    boundaryrt()

    boundarydwn()

    collide()

    collid()

    collid1()

    collide1()

    collid2()

    collide2()

    b11.goto(x2,y2)

    boundaryup()

    boundarylt()

    boundaryrt()

    boundarydwn()

    collide()

    collid()

    collid1()

    collide1()

    collid2()

    collide2()

    b22.goto(x11,y11)

    boundaryup()

    boundarylt()

    boundaryrt()

    boundarydwn()

    collide()

    collid()

    collid1()

    collide1()

    collid2()

    collide2()

    b12.goto(x3,y3)

    boundaryup()

    boundarylt()

    boundaryrt()

    boundarydwn()

    collide()

    collid()

    collid1()

    collide1()

    collid2()

    collide2()

    b23.goto(x12,y12)

    boundaryup()

    boundarylt()

    boundaryrt()

    boundarydwn()

    time.sleep(0.5)

    #restrictions

    collid()

    collid1()

    collide()

    collide1()

    collid2()

    collide2()

    boundaryup()

    boundarylt()

    boundaryrt()

    boundarydwn()

    collide()

    collid()

    collid1()

    collide1()

    collid2()

    collide2()

    #hide

    b1.hideturtle()

    b2.hideturtle()

    b11.hideturtle()

    b22.hideturtle()

    b12.hideturtle()

    b23.hideturtle()

    boundaryup()

    boundarylt()

    boundaryrt()

    boundarydwn()

    #return

    b1.goto(-240,170)

    b2.goto(240,170)

    b11.goto(-240,170)

    b22.goto(240,170)

    b12.goto(-240,170)

    b23.goto(240,170)

    boundaryup()

    boundarylt()

    boundaryrt()

    boundarydwn()

    score += 10
    s2.undo()

    s2.penup()

    s2.goto(0,110)

    scoreq = "SCORE: %s" %score

    s2.write( scoreq , False , align = 'center' , font = ('Arial' , 32 , 'underline'))