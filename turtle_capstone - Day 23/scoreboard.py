from turtle import Turtle


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

    def game_over(self):
        self.goto(-150, 0)
        self.write("Game Over, my boi...", move=False, font=FONT)





