from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Study Counter')
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
checkmark = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, 'bold'))
checkmark.grid(column=1, row=3)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)
start_button.grid(column=0, row=2)
reset_button = Button(text='Reset')
reset_button.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_ing = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_ing)
timer_text = canvas.create_text(100, 130, text='00:00', fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)














window.mainloop()
