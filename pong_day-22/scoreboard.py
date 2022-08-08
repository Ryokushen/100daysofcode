from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, coord_x, coord_y):
        super().__init__()
        self.starting_score = 0
        self.goto(coord_x, coord_y)
        self.ht()
        self.penup()
        self.color('white')
        self.write(self.starting_score, align='right', font=('arial', 40, 'bold'))

    def increase_score(self):
        self.clear()
        self.starting_score += 1
        self.write(self.starting_score, align='right', font=('arial', 40, 'bold'))

