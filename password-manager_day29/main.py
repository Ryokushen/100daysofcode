from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ------------------------------Password Data Entry--------------------------------#


def data_entry():
    website = input_website.get()
    email = input_email.get()
    password_create = input_password.get()

    if len(website) and len(password_create) and len(email) != 0:
        is_ok = messagebox.askokcancel(title=website, message=f"Is this data correct?:\nEmail: {email} "
                                                          f"\nPassword: {password_create}")
        with open("data.txt", "a") as template:
            template.write(f"{website} | {email} | {password_create} \n")
            delete()
    else:
        messagebox.showwarning(title="Empty Input",
                                message='Please don\'t leave any necessary fields empty.')


def delete():
    input_website.delete(0, END)
    input_password.delete(0, END)

# -------------------------------Password Generator--------------------------------#


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [(choice(letters)) for _ in range(randint(6, 8))]
    password_list += [(choice(symbols)) for _ in range(randint(2, 4))]
    password_list += [(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)
# --------------------------UI SETUP-----------------------------------#


window = Tk()

window.title('The Saiyan Vault')
window.config(padx=40, pady=20, bg='black')


canvas = Canvas(width=186, height=150, background='royalblue', highlightthickness=8, highlightbackground='royalblue')
passwordgen = PhotoImage(file='saiyanvault1.png')
canvas.create_image(100, 81, image=passwordgen)
canvas.grid(column=1, row=0)

saiyan = Label(text="Retain the power,\n unleash the fury.\nThere is no \nescaping the vault...", font=("Harrington", 12, "italic"), fg="royalblue", bg='black')
saiyan.grid(column=0, row=0)

website_label = Label(text='Website:', bg="black", font=("Courier", 12, 'bold'), fg='royalblue')
website_label.grid(column=0, row=1)
input_website = Entry(width=56)
input_website.focus()
input_website.grid(row=1, column=1, columnspan=2)

email_usn = Label(text="Email/Username:", bg="black", font=("Courier", 12, 'bold'), fg='royalblue')
email_usn.grid(column=0, row=2)
input_email = Entry(width=56)
input_email.insert(0, "example@gmail.com")
input_email.grid(row=2,column=1, columnspan=2)

password = Label(text="Password:", bg="black", font=("Courier", 12, 'bold'), fg='royalblue')
password.grid(column=0, row=3)
input_password = Entry(width=37)
input_password.grid(column=1, row=3)

add_button = Button(text="Add", width=47, command=data_entry)
add_button.grid(row=4, column=1, columnspan=2)

generate_pass = Button(text="Generate Password", height=1, command=generate_password)
generate_pass.grid(column=2, row=3)


window.mainloop()