from tkinter import *
from random import choice
import pandas

to_learn = {}
current_card = {}
BACKGROUND_COLOR = "#B1DDC6"


try:
    french_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = french_data.to_dict(orient='records')



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(canvas_start, image=front_card)
    flip_timer = window.after(3000, func=flip_card)
    print(len(to_learn))



def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(canvas_start, image=back_card)

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")


window = Tk()
window.title("Flash Card Capstone")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)


flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)

back_card = PhotoImage(file='images/card_back.png')
back_side = canvas.create_image(400, 263, image=back_card)


front_card = PhotoImage(file="images/card_front.png")
wrong = PhotoImage(file="images/wrong.png")
right = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong, highlightthickness=0,  bg=BACKGROUND_COLOR, command=next_card)
right_button = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)

canvas_start = canvas.create_image(400, 263, image=front_card)


canvas.grid(column=0, row=0, columnspan=2)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

card_title = canvas.create_text(400, 150,font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "italic"))


next_card()

























window.mainloop()













