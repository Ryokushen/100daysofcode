from turtle import Turtle,Screen

X_POSITION = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()


class Snake:

    def __init__(self):
        self.body = []
        for snake_index in range(0, 3):
            self.snake = Turtle(shape='square')
            self.color = self.snake.color('white')
            self.body.append(self.snake)
            self.snake.penup()
            self.snake.goto(x=X_POSITION[snake_index], y=0)

    def movement(self):
        for snake_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[snake_num - 1].xcor()
            new_y = self.body[snake_num - 1].ycor()
            self.body[snake_num].goto(new_x, new_y)
        self.body[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.body[0].heading() != DOWN:
            self.body[0].setheading(UP)

    def down(self):
        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)

    def right(self):
        if self.body[0].heading() != LEFT:
            self.body[0].setheading(RIGHT)

    def left(self):
        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)


