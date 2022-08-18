from tkinter import *

# Create window object, change title and manipulate size
window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)


# Label

my_label = Label(text='I Am a Label', font=('Arial', 24, 'bold'))
my_label.pack()


my_label.config(text='New Text')


# Button

def button_clicked():
    print('I got clicked')
    my_label.config(text=f'{ input.get()}')


button = Button(text='Click Me', command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()





window.mainloop()