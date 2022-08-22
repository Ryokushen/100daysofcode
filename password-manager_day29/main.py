from tkinter import *

#--------------------------UI SETUP-----------------------------------#
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg='lightblue')


canvas = Canvas(width=350, height=350, bg='lightblue', highlightthickness=10, highlightbackground='grey')
passwordgen = PhotoImage(file='python.png.png')
canvas.create_image(175, 175, image=passwordgen)
canvas.grid(column=1, row=1)
























window.mainloop()