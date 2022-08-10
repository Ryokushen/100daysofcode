import time

from turtle import Screen
from player import Player, FINISH_LINE_Y
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()

screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

# Player movement across level
    screen.onkeypress(player.movement, 'Up')

# Player beats level and resets to new level
    if player.ycor() >= FINISH_LINE_Y:
        player.starting_position()
        scoreboard.update_score()

















screen.exitonclick()