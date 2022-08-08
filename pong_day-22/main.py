from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("Welcome to the Pong Zone")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()

l_score = Scoreboard(-50, 240)
r_score = Scoreboard(50, 240)

screen.listen()
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')

screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')

game_is_on = True
varied_time = 0.1

while game_is_on:
    time.sleep(varied_time)
    screen.update()
    ball.ball_move()
    print(ball.xcor())
    # Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        varied_time -= 0.001

    # Increase Score
    if ball.xcor() < -380:
        r_score.increase_score()
        ball.reset_ball()
        varied_time = 0.1

    if ball.xcor() > 380:
        l_score.increase_score()
        ball.reset_ball()
        varied_time = 0.1


screen.exitonclick()
