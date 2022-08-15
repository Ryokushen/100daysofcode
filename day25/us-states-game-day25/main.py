import turtle
import pandas
from mapped_states import State

# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = 'blank_states_img.gif'
# screen.addshape(image)
# turtle.shape(image)


data = pandas.read_csv('50_states.csv')
data_states = data.state
list_of_states = data_states.to_list()

print(state_xcoord)
correct = []
game_is_on = True

while game_is_on:

    answer_state = screen.textinput(title="Guess the State!", prompt="What's another state's name?").title()
    for state in list_of_states:
        if state == answer_state:
            state_xcoord = data[data_states == state].x
            state_ycoord = data[data_states == state].y

            correct.append(state)
            writing = State()
            writing.goto()
            print(correct)



