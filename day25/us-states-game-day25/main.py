import turtle
import pandas
from mapped_states import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
screen.setup(width=750, height=525)
turtle.shape(image)

# Turn CSV Series into list
data = pandas.read_csv('50_states.csv')
data_states = data.state
list_of_states = data_states.to_list()

correct = []


while len(correct) < 50:
    answer_state = screen.textinput(title=f'{len(correct)}/50 Correct', prompt="What's another state's name?").title()
    for state in list_of_states:
        # Compare input to list of states in CSV
        if state == answer_state:
            # Write state name on coords on map
            state_xcoord = int(data[data_states == state].x)
            state_ycoord = int(data[data_states == state].y)
            # Add correct guess to list to keep track of score
            correct.append(state)
            writing = State()
            writing.goto(x=state_xcoord, y=state_ycoord)
            writing.write(f'{state}')
        else:
            continue


screen.exitonclick()