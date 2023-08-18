import random
from tkinter import *
import pandas as pd
from tkinter import messagebox

data_dict = []

BACKGROUND_COLOR = "#B1DDC6"


def generate_data():
    global data_dict
    df = pd.read_csv("data/french_words.csv")
    data_dict = df.to_dict(orient="records")


generate_data()


def correct_answer():
    data = next_card()
    data_dict.remove(data)
    print(len(data_dict))
    if len(data_dict) == 0:
        messagebox.showinfo(title="Congratulations!!!", message="You've memorized all the items in the flash card.")
        generate_data()


def wrong_answer():
    next_card()


def next_card():
    rand_data = random.choice(data_dict)
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(language, text=list(rand_data.keys())[0], fill="black")
    canvas.itemconfig(translated_text, text=rand_data[list(rand_data.keys())[0]], fill="black")
    window.after(3000, flip_card, rand_data)
    return rand_data


def flip_card(data):
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(language, text=list(data.keys())[1], fill="white")
    canvas.itemconfig(translated_text, text=data[list(data.keys())[1]], fill="white")


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

card_image = canvas.create_image(400, 263, image=card_front_img)
language = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
translated_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

x_button_img = PhotoImage(file="./images/wrong.png")
v_button_img = PhotoImage(file="./images/right.png")

right_button = Button(image=v_button_img, borderwidth=0, highlightthickness=0, command=correct_answer)
right_button.grid(row=1, column=1)

wrong_button = Button(image=x_button_img, borderwidth=0, highlightthickness=0, command=wrong_answer)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
