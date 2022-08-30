from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flash Card Capstone")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)













canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
front_card = PhotoImage(file="images/card_front.png")
wrong = PhotoImage(file="images/wrong.png")
right = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong, highlightthickness=0,  bg=BACKGROUND_COLOR)
right_button = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR)

canvas.create_image(400, 263, image=front_card)


canvas.grid(column=0, row=0, columnspan=2)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)






























window.mainloop()













