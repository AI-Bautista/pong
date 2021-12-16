# This is the beningging of Pong
# by Bautista and Montesa

import turtle as t

window = t.Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width = 1280, height = 720)
window.tracer(0)
# window.exitonclick() #Exit window when screen is clicked

while True:
    window.update()