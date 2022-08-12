from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.ht()
        self.penup()
        self.speed('fastest')
        self.score = 0
        with open('data.txt') as data:
            self.highscore = int(data.read())
        self.goto(100, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False,
                   align='right', font=('Arial', 16, 'bold'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.highscore}')
        self.score = 0
        self.update_scoreboard()



    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto((150, 0))
    #     self.write(f"GAME OVER. Tsk, Tsk, Tsk. ", False,
    #                align='right', font=('Arial', 18, 'bold'))
