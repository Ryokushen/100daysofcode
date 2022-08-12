from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.ht()
        self.penup()
        self.speed('fastest')
        self.counter = 0
        self.goto(50, 275)
        self.write(f"Score: {self.counter} ", False, align='right', font=('Arial', 16, 'bold'))

    def increase_score(self):
        self.clear()
        self.counter += 1
        self.write(f"Score: {self.counter} ", False, align='right', font=('Arial', 14, 'bold'))

    def game_over(self):
        self.goto((150, 0))
        self.write(f"GAME OVER. Tsk, Tsk, Tsk. ", False, align='right', font=('Arial', 18, 'bold'))
