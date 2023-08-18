import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv("data/french_words.csv")
data_dict = df.to_dict(orient="records")


def next_card():
    rand_data = random.choice(data_dict)
    canvas.itemconfig(language, text=list(rand_data.keys())[0])
    canvas.itemconfig(translated_text, text=rand_data[list(rand_data.keys())[0]])


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

canvas.create_image(400, 263, image=card_front_img)
language = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
translated_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

x_button_img = PhotoImage(file="./images/wrong.png")
v_button_img = PhotoImage(file="./images/right.png")

right_button = Button(image=v_button_img, borderwidth=0, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

wrong_button = Button(image=x_button_img, borderwidth=0, highlightthickness=0)
wrong_button.grid(row=1, column=0)

next_card()
window.mainloop()
