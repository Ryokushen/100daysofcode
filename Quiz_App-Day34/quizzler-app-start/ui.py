from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, columnspan=2,row=1, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)

        true_image = PhotoImage(file="images/true.png")
        self.correct_btn = Button(image=true_image, command=self.trueanswer)
        self.correct_btn.grid(column=0, row=2)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_image, command=self.falseanswer)
        self.wrong_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.correct_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def trueanswer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

        self.score_label.config(text=f"Score: {self.quiz.score}")


    def falseanswer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)









