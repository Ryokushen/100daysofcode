from turtle import Turtle
from random import choice, random, randrange

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(-180)
        self.color(choice(COLORS))
        self.goto(300, (randrange(-230, 230)))


    def car_drive(self):
        self.fd(MOVE_INCREMENT)

    def car_reset(self):
        self.goto(300, (randrange(-230, 230)))


