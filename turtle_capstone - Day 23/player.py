from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape='turtle')
        self.penup()
        self.color('black')
        self.starting_position()

    def movement(self):
        self.fd(MOVE_DISTANCE)

    def starting_position(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)

