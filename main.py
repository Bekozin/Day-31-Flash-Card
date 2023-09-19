from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
dict = data.to_dict(orient="records")

selection = {}


def next_card():
    global selection, flip_timer
    window.after_cancel(flip_timer)
    selection = random.choice(dict)
    canvas.itemconfig(title_card, text="French", fill="black")
    canvas.itemconfig(word_card, text=selection["French"], fill="black")
    canvas.itemconfig(background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_card, text="English", fill="white")
    canvas.itemconfig(word_card, text=selection["English"], fill="white")
    canvas.itemconfig(background, image=background_image)


window = Tk()

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='images/card_front.png')
background_image = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 263, image=card_front_img)
title_card = canvas.create_text(400, 150, text='', font=("Ariel", 40, "italic"))
word_card = canvas.create_text(400, 263, text='', font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

cross = PhotoImage(file="images/wrong.png")
unkown_button = Button(image=cross, highlightthickness=0, command=next_card)
unkown_button.grid(row=1, column=0)

check = PhotoImage(file="images/right.png")
known_button = Button(image=check, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=2)

next_card()

window.mainloop()
