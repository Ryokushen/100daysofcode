from tkinter import *

def button_clicked():
    print('Converting....')
    math_button.config(text=f'{ round(int(input.get()) * 1.6, 1) }')


# Create window object, change title and manipulate size
window = Tk()
window.title('My First GUI Program')
window.minsize(width=350, height=200)
window.config(padx=50, pady=50)


# Labels
miles = Label(text='Miles', font=('Arial', 12, 'bold'))
miles.grid(column=6, row=2)

equal = Label(text='is equal to', font=('Arial', 12, 'bold'))
equal.grid(column=4, row=4)

kilometer = Label(text='KM', font=('Arial', 12, 'bold'))
kilometer.grid(column=6, row=4)

# Button
button = Button(text='Calculate', command=button_clicked)
button.grid(column=5, row=5)

math_button = Label(text=0, font=("Arial", 12, 'bold'))
math_button.grid(column=5, row=4)

# Entry
input = Entry(width=10)
input.grid(column=5, row=2)





window.mainloop()