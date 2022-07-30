# import colorgram
#
# colors = colorgram.extract('painting.jpg', 15)
# print(colors)
#
# list_of_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     list_of_colors.append(new_color)
#
# print(list_of_colors)


from random import choice
from turtle import Turtle, Screen

color_list = [(234, 233, 232), (235, 232, 234), (230, 233, 237), (226, 233, 229), (224, 157, 75), (31, 105, 150), (14, 53, 90), (162, 18, 43), (228, 209, 98), (169, 92, 31), (124, 182, 209), (203, 163, 19), (180, 43, 87), (125, 197, 147), (39, 140, 31)]


timmy = Turtle()

timmy.shape('turtle')
timmy.color('black')
timmy.speed('slow')
viewers = Screen()

viewers.colormode(255)


def color_choice():
    selection = choice(color_list)
    r = selection[0]
    g = selection[1]
    b = selection[2]
    iteration = (r, g, b)
    return iteration


def y_type():
    timmy.goto(0.0, timmy.ycor() + 50)


def move():
    timmy.up()
    for _ in range(10):
        timmy.showturtle()
        timmy.dot(20)
        timmy.pencolor((color_choice()))
        timmy.hideturtle()
        timmy.fd(50)


for _ in range(10):
    move()
    y_type()
    timmy.rt(360)

viewers.exitonclick()




