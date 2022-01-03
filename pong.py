# This is the beningging of Pong
# by Bautista and Montesa

import turtle as t

window = t.Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width = 1280, height = 720)
window.tracer(0)

rightbar = t.Turtle()
rightbar.color("blue")
rightbar.shape("square")
rightbar.shapesize(barwid = 6, barlen = 1)
rightbar.goto(550, 0)
rightbar.dy = -1
rightbar.speed(0)
rightbar.penup()

leftbar = t.Turtle()
leftbar.color("red")
leftbar.shape("square")
leftbar.shapesize(barwid = 6, barlen = 1)
leftbar.goto(-550, 0)
leftbar.dy = -1
leftbar.speed(0)
leftbar.penup()

def rightbar_up():
    y = rightbar.ycor()
    y += 25   # add 25 pixels to the y coordinates when going up
    rightbar.sety(y)
    rightbar.sety(rightbar.ycor() + rightbar.dy)
    if rightbar.ycor() > 170:   # restricts the bar from going off the screen
        rightbar.sety(170)
        rightbar.dy *= -1
        
def rightbar_down():
    y = rightbar.ycor()
    y -= 25
    rightbar.sety(y)
    rightbar.sety(rightbar.ycor() + rightbar.dy)
    if rightbar.ycor() > -300:
        rightbar.sety(-300)
        rightbar.dy *= -1

def leftbar_up():
    y = leftbar.ycor()
    y += 25 
    leftbar.sety(y)
    leftbar.sety(leftbar.ycor() + leftbar.dy)
    if leftbar.ycor() > 170:
        leftbar.sety(170)
        leftbar.dy *= -1
        
def leftbar_down():
    y = leftbar.ycor()
    y -= 25
    leftbar.sety(y)
    leftbar.sety(leftbar.ycor() + leftbar.dy)
    if leftbar.ycor() > -300:
        leftbar.sety(-300)
        leftbar.dy *= -1

window.listen()
window.onkeypress(rightbar_up, "Up")
window.onkeypress(rightbar_down, "Down")
window.onkeypress(leftbar_up, "w")
window.onkeypress(leftbar_down, "s")

while True:
    window.update()
