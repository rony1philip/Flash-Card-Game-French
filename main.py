from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
f_word = ''
e_txt = 'bla'

# ------------------------------------------------RANDOM WORD--------------------------------------------------------#

data = pandas.read_csv('data/french_words.csv')
french_words = data['French'].to_list()
french_words_dicts = data.to_dict(orient='records')


def next_card():
    current_card = random.choice(french_words_dicts)
    canvas_f.itemconfig(card_title, text='French')
    canvas_f.itemconfig(f_random_word, text=current_card['French'])


# ----------------------------------------------------UI---------------------------------------------------------------#
window = Tk()
window.title('Flash Card Game')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(800, 526)

canvas_f = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file='C:/Users/user/Desktop/flash-card-project-start/images/card_front.png')
canvas_f.create_image(405, 263, image=front_img)
card_title = canvas_f.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
f_random_word = canvas_f.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas_f.grid(row=1, column=1, columnspan=2)

# canvas_b = Canvas(width=800, height=526, bg=BACKGROUND_COLOR ,highlightthickness=0)
# back_img = PhotoImage(file='C:/Users/user/Desktop/flash-card-project-start/images/card_back.png')
# canvas_b.create_image(400, 263, image=back_img)
# canvas_b.create_text(405,150,text='English', font=('Ariel', 40, 'italic'))
# canvas_b.create_text(405,263, text=e_text, font=('Ariel', 60, 'bold') )
# canvas_b.grid(row= 1, column=1, columnspan=2)

v_img = PhotoImage(file='C:/Users/user/Desktop/flash-card-project-start/images/right.png')
v_b = Button(image=v_img, highlightthickness=0, command=next_card)
v_b.grid(row=2, column=2)

x_img = PhotoImage(file='C:/Users/user/Desktop/flash-card-project-start/images/wrong.png')
x_b = Button(image=x_img, highlightthickness=0)
x_b.grid(row=2, column=1)

next_card()

window.mainloop()
