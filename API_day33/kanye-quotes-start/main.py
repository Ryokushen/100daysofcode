from tkinter import *
import requests


def get_quote():
    pulled_quote = requests.get('https://api.kanye.rest')
    pulled_quote.raise_for_status()
    cleaned_quote = pulled_quote.json()['quote']
    canvas.itemconfig(quote_text, text=cleaned_quote, font=("Arial", 20, "bold"), fill="black")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye West says...", width=250, font=("Arial", 30, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
