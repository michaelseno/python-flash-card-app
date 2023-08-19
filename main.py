import random
from tkinter import *
import pandas as pd
import os
from tkinter import messagebox

data_dict = []
current_card = {}
path = ""

BACKGROUND_COLOR = "#B1DDC6"


def update_card_list():
    data_dict.remove(current_card)
    df = pd.DataFrame(data_dict)
    df.to_csv("data/words_to_learn.csv", index=False)


def generate_data():
    try:
        global data_dict, path
        if os.path.exists("data/words_to_learn.csv"):
            path = "data/words_to_learn.csv"
        else:
            path = "data/french_words.csv"

        df = pd.read_csv(path)
        data_dict = df.to_dict(orient="records")
    except pd.errors.EmptyDataError:
        os.remove(path="data/words_to_learn.csv")
        generate_data()


def correct_answer():
    update_card_list()
    next_card()


def wrong_answer():
    next_card()


def next_card():
    try:
        global current_card, flip_timer
        window.after_cancel(flip_timer)
        current_card = random.choice(data_dict)
        canvas.itemconfig(card_image, image=card_front_img)
        canvas.itemconfig(language, text=list(current_card.keys())[0], fill="black")
        canvas.itemconfig(translated_text, text=current_card[list(current_card.keys())[0]], fill="black")
        print(current_card)
        flip_timer = window.after(3000, func=flip_card)
    except IndexError:
        messagebox.showinfo(title="Congratulations!", message=f"You've Memorized all of the words in the list.")
        os.remove(path="data/words_to_learn.csv")
        generate_data()


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(language, text=list(current_card.keys())[1], fill="white")
    canvas.itemconfig(translated_text, text=current_card[list(current_card.keys())[1]], fill="white")


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

generate_data()

flip_timer = window.after(3000, func=flip_card)

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
