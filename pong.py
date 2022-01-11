# This is the beningging of Pong
# by Bautista and Montesa

import turtle as t

window = t.Screen()
window.title("Ping Pong Game")
window.bgcolor("#1F6420")
window.setup(width = 1280, height = 720)
window.tracer(0)

rightbar = t.Turtle()
rightbar.penup()
rightbar.color("blue")
rightbar.shape("square")
rightbar.shapesize(6,1)
rightbar.goto(550, 0)
rightbar.dy = -1
rightbar.speed(0)


leftbar = t.Turtle()
leftbar.penup()
leftbar.color("red")
leftbar.shape("square")
leftbar.shapesize(6,1)
leftbar.goto(-550, 0)
leftbar.dy = -1
leftbar.speed(0)

# middlebar = t.Turtle()
# middlebar.penup()
# middlebar.shape("square")
# middlebar.shapesize(t.window_height(),0.1)
# middlebar.goto(-1,-1)

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

#Left Player
def rightbar_up():
    y = rightbar.ycor()
    y += 25   # add 25 pixels to the y coordinates when going up
    rightbar.sety(y)
    rightbar.sety(rightbar.ycor() + rightbar.dy)
    if rightbar.ycor() > 300:   # restricts the bar from going off the screen
        rightbar.sety(300)
        rightbar.dy *= -1
        
def rightbar_down():
    y = rightbar.ycor()
    y -= 25
    rightbar.sety(y)
    rightbar.sety(rightbar.ycor() + rightbar.dy)
    if rightbar.ycor() < -300:
        rightbar.sety(-300)
        rightbar.dy *= -1

#Right Player
def leftbar_up():
    y = leftbar.ycor()
    y += 25 
    leftbar.sety(y)
    leftbar.sety(leftbar.ycor() + leftbar.dy)
    if leftbar.ycor() > 300:
        leftbar.sety(300)
        leftbar.dy *= -1
        
def leftbar_down():
    y = leftbar.ycor()
    y -= 25
    leftbar.sety(y)
    leftbar.sety(leftbar.ycor() + leftbar.dy)
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
