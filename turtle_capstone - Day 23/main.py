import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from scoreboard import Scoreboard
from car_manager import Car

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()


screen.listen()

lst = []
drivers_list = []
game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

# Move the cars and reset them after they go off-screen
    for i in range(0, len(drivers_list)):
        drivers_list[i].car_drive()
        if drivers_list[i].xcor() < -320:
            drivers_list[i].car_reset()

# Generate new car every 6 game loops (kinda clunky but, it works)
    lst.append(screen.update)
    update_counter = len(lst)
    if (update_counter % 6) == 0 and len(drivers_list) < 30:
        drivers_list.append(Car())

# Player movement across level
    screen.onkeypress(player.movement, 'Up')

# Player beats level and resets to new level
    if player.ycor() >= FINISH_LINE_Y:
        player.starting_position()
        scoreboard.update_score()
        if i in range(0, len(drivers_list)):
            drivers_list[i].increase_speed()

# Detect collisions
    for i in range(0, len(drivers_list)):
        if player.distance(drivers_list[i]) < 15:
            game_is_on = False















screen.exitonclick()
