from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.ht()
        self.penup()
        self.speed('fastest')
        self.score = 0
        self.highscore = 0
        self.goto(50, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} ", False,
                   align='right', font=('Arial', 16, 'bold'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} ", False,
                   align='right', font=('Arial', 14, 'bold'))

    def game_over(self):
        self.goto((150, 0))
        self.write(f"GAME OVER. Tsk, Tsk, Tsk. ", False,
                   align='right', font=('Arial', 18, 'bold'))
