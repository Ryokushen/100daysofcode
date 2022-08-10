from turtle import Turtle
from player import Player

FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.pencolor('black')
        self.goto(-280, 260)
        self.level = 1
        self.score()

    def score(self):
        self.write(f'Level: {self.level}', move=False, font=FONT)

    def update_score(self):
        self.clear()
        self.level += 1
        self.score()
