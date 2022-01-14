# This is the beningging of Pong
# by Bautista and Montesa

import turtle as t
import time as c

window = t.Screen()
window.title("Ping Pong Game")
window.bgcolor("#1F6420")
window.setup(width = 1280, height = 720)
window.tracer(0)

def mouseClick(x,y):
    print("X = {0}, Y = {1}".format(x,y))

t.onscreenclick(mouseClick,1)

rightbar = t.Turtle()
rightbar.penup()
rightbar.color("blue")
rightbar.shape("square")
rightbar.shapesize(5,1)
rightbar.goto(500, 0)
rightbar.speed(0)
rightbar.dy = 1


leftbar = t.Turtle()
leftbar.penup()
leftbar.color("red")
leftbar.shape("square")
leftbar.shapesize(5,1)
leftbar.goto(-500, 0)
leftbar.speed(0)
leftbar.dy = 1

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
ball.dx = 9
ball.dy = 9


#Scoring
player1Score = 0
player2Score = 0


leftScore = t.Turtle()
leftScore.speed(0)
leftScore.color("White")
leftScore.penup()
leftScore.hideturtle()
leftScore.goto(-150,t.window_height()/2.5)
leftScore.write("{}".format(player2Score), move=True, font=("Verdana", 40, "bold"))

rightScore = t.Turtle()
rightScore.speed(0)
rightScore.color("White")
rightScore.penup()
rightScore.hideturtle()
rightScore.goto(105,t.window_height()/2.5)
rightScore.write("{}".format(player2Score), move=True, font=("Verdana", 40, "bold"))

# Bars movement restrictions 
# Right Player
def rightbar_up(speed):
    y = rightbar.ycor()
    y += speed   # add 25 pixels to the y coordinates when going up
    rightbar.sety(y)
    if rightbar.ycor() > 200:   # restricts the bar from going off the screen
        rightbar.sety(200)
        rightbar.dy *= -1
        
def rightbar_down(speed):
    y = rightbar.ycor()
    y -= speed
    rightbar.sety(y)
    if rightbar.ycor() < -250:
        rightbar.sety(-250)
        rightbar.dy *= -1

# Left Player
def leftbar_up():
    y = leftbar.ycor()
    y += 20 
    leftbar.sety(y)
    if leftbar.ycor() > 200:
        leftbar.sety(200)
        leftbar.dy *= -1
        
def leftbar_down():
    y = leftbar.ycor()
    y -= 20
    leftbar.sety(y)
    if leftbar.ycor() < -250:
        leftbar.sety(-250)
        leftbar.dy *= -1

window.listen()
# window.onkeypress(rightbar_up, "Up")
# window.onkeypress(rightbar_down, "Down")
window.onkeypress(leftbar_up, "w")
window.onkeypress(leftbar_down, "s")

while True:
    window.update()
    c.sleep(1/144)
    print(ball.dx)
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
    
    # left
    if ball.xcor() < -560:
        ball.goto(0,0)
        ball.dx = 9
        ball.dx *= -1
        player2Score += 1
        rightScore.undo()
        rightScore.write("{}".format(player2Score), move=True, font=("Verdana", 40, "bold"))

    # right
    if ball.xcor() > 560:
        ball.goto(0,0)
        ball.dx = 9
        ball.dx *= -1
        player1Score += 1
        leftScore.undo()
        leftScore.write("{}".format(player1Score), move=True, font=("Verdana", 40, "bold"))

                
    # ball conditions when hitting the bars
    if (ball.xcor() > rightbar.xcor() - 30 and ball.xcor() < rightbar.xcor()) and (ball.ycor() < rightbar.ycor()+55 and ball.ycor() > rightbar.ycor()-55):
        if (ball.dx <= 60):
            ball.dx += 2
        ball.dx*= -1
            
    if (ball.xcor() < leftbar.xcor() + 30 and ball.xcor() > leftbar.xcor()) and (ball.ycor() < leftbar.ycor()+55 and ball.ycor()>leftbar.ycor()-55):
        if (ball.dx >= -60):
            ball.dx -= 2
        ball.dx*= -1

    #AI for player 2 / Right paddle
    if (ball.ycor() > rightbar.ycor()):
        rightbar_up(7)
    if (ball.ycor() < rightbar.ycor()):
        rightbar_down(7)

    # if (ball.ycor() > leftbar.ycor()):
    #     leftbar_up()
    # if (ball.ycor() < leftbar.ycor()):
    #     leftbar_down()
