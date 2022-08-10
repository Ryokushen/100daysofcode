from turtle import Turtle
from random import choice, randrange

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class Car(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(-180)
        self.color(choice(COLORS))
        self.goto(300, (randrange(-230, 230)))

    def car_drive(self):
        self.fd(STARTING_MOVE_DISTANCE)

    def car_reset(self):
        self.goto(300, (randrange(-230, 230)))

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT



