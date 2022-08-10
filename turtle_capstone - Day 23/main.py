import time

from player import Turtle, Screen

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)







game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

















screen.exitonclick()