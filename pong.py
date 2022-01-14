# This is the beningging of Pong
# by Bautista and Montesa

import turtle as t
import time as c

window = t.Screen()
window.title("Ping Pong Game")
window.bgcolor("#1F6420")
window.setup(width = 1280, height = 720)
window.tracer(0)

rightbar = t.Turtle()
rightbar.penup()
rightbar.color("blue")
rightbar.shape("square")
rightbar.shapesize(5,1)
rightbar.goto(500, 0)
rightbar.speed(0)


leftbar = t.Turtle()
leftbar.penup()
leftbar.color("red")
leftbar.shape("square")
leftbar.shapesize(5,1)
leftbar.goto(-500, 0)
leftbar.speed(0)

# middlebar = t.Turtle()
# middlebar.penup()
# middlebar.shape("square")
# middlebar.shapesize(t.window_height(),0.1)
# middlebar.goto(-1,-1)

ball = t.Turtle()
ball.speed("fast")
ball.penup()
ball.shape("circle")
ball.shapesize(2,2)
ball.color("yellow")
ball.goto(0,0)
ball.dx = 15
ball.dy = 15

#Scoring
player1Score = 0
player2Score = 0


leftScore = t.Turtle()
leftScore.penup()
leftScore.goto(-150,t.window_height()/2.5)
leftScore.write(player1Score, move=True, font=("Verdana", 40, "bold"))


rightScore = t.Turtle()
rightScore.penup()
rightScore.goto(105,t.window_height()/2.5)
rightScore.write(player2Score, move=True, font=("Verdana", 40, "bold"))

# Bars movement restrictions 
# Right Player
def rightbar_up():
    y = rightbar.ycor()
    y += 50   # add 25 pixels to the y coordinates when going up
    rightbar.sety(y)
    if rightbar.ycor() > 200:   # restricts the bar from going off the screen
        rightbar.sety(200)
        rightbar.dy *= -1
        
def rightbar_down():
    y = rightbar.ycor()
    y -= 50
    rightbar.sety(y)
    if rightbar.ycor() < -300:
        rightbar.sety(-300)
        rightbar.dy *= -1

# Left Player
def leftbar_up():
    y = leftbar.ycor()
    y += 50 
    leftbar.sety(y)
    if leftbar.ycor() > 200:
        leftbar.sety(200)
        leftbar.dy *= -1
        
def leftbar_down():
    y = leftbar.ycor()
    y -= 50
    leftbar.sety(y)
    if leftbar.ycor() < -300:
        leftbar.sety(-300)
        leftbar.dy *= -1

window.listen()
window.onkeypress(rightbar_up, "Up")
window.onkeypress(rightbar_down, "Down")
window.onkeypress(leftbar_up, "w")
window.onkeypress(leftbar_down, "s")

while True:
    window.update()
    c.sleep(1/60)
    
    ball.setx(ball.xcor()+ball.dx/2)
    ball.sety(ball.ycor()+ball.dy/2)
    
    # Ball movement restrictions
    # up
    if ball.ycor() > 200:
        ball.sety(200)
        ball.dy *= -1
    # down
    if ball.ycor() < -300: 
        ball.sety(-300)
        ball.dy *= -1
    
    # right
    if ball.xcor() < -570:
        ball.goto(0,0)
        ball.dy *= -1

    # left
    if ball.xcor() > 570:
        ball.goto(0,0)
        ball.dy *= -1
        
    # ball conditions when hitting the bars
    if (ball.xcor() > 455 and ball.xcor() < 465) and (ball.ycor() < rightbar.ycor()+40 and ball.ycor() > rightbar.ycor()-40):
        ball.setx(455) 
        ball.dx*=-1

    if (ball.xcor() < -455 and ball.xcor() > -465) and (ball.ycor() < leftbar.ycor()+40 and ball.ycor()>leftbar.ycor()-40):
        ball.setx(-455)
        ball.dx*=-1
    
    
    
    
    
    
    
