from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coord_x, coord_y):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coord_x, coord_y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)





