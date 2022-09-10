from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, columnspan=2,row=1, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"))

        true_image = PhotoImage(file="images/true.png")
        self.correct_btn = Button(image=true_image)
        self.correct_btn.grid(column=0, row=2)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_image)
        self.wrong_btn.grid(column=1, row=2)


        self.window.mainloop()
