BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

canvas.create_image(400, 263, image=card_front_img)
language = canvas.create_text(400, 150, text="Language", fill="black", font=("Arial", 40, "italic"))
translated_text = canvas.create_text(400, 263, text="to be Translated", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

x_button_img = PhotoImage(file="./images/wrong.png")
v_button_img = PhotoImage(file="./images/right.png")

right_button = Button(image=v_button_img, borderwidth=0, highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_button = Button(image=x_button_img, borderwidth=0, highlightthickness=0)
wrong_button.grid(row=1, column=0)
window.mainloop()



