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

guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 Correct', prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        break
    for state in list_of_states:
        # Compare input to list of states in CSV
        if state == answer_state:
            # Write state name on coords on map
            state_xcoord = int(data[data_states == state].x)
            state_ycoord = int(data[data_states == state].y)
            # Add correct guess to list to keep track of score
            guessed_states.append(state)
            writing = State()
            writing.goto(x=state_xcoord, y=state_ycoord)
            writing.write(f'{state}')

# Makes list of states you miss
missed_states = []
for state in list_of_states:
    if state not in guessed_states:
        missed_states.append(state)
        states_to_learn = pandas.DataFrame(missed_states)
        states_to_learn.to_csv('states_to_learn.csv')


