from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
f_text = ''
e_txt= 'bla'
# ----------------------------------------------------UI--------------------------------------------------------------#
window = Tk()
window.title('Flash Card Game')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(800,526)

canvas_f = Canvas(width=800, height=526, bg=BACKGROUND_COLOR ,highlightthickness=0)
front_img = PhotoImage(file='C:/Users/user/Desktop/flash-card-project-start/images/card_front.png')
canvas_f.create_image(405, 263, image=front_img)
canvas_f.create_text(400,150,text='French', font=('Ariel', 40, 'italic'))
canvas_f.create_text(400,263, text=f_text, font=('Ariel', 60, 'bold') )
canvas_f.grid(row= 1, column=1, columnspan=2)

# canvas_b = Canvas(width=800, height=526, bg=BACKGROUND_COLOR ,highlightthickness=0)
# back_img = PhotoImage(file='C:/Users/user/Desktop/flash-card-project-start/images/card_back.png')
# canvas_b.create_image(400, 263, image=back_img)
# canvas_b.create_text(405,150,text='English', font=('Ariel', 40, 'italic'))
# canvas_b.create_text(405,263, text=e_text, font=('Ariel', 60, 'bold') )
# canvas_b.grid(row= 1, column=1, columnspan=2)

v_img = PhotoImage(file='C:/Users/user/Desktop/flash-card-project-start/images/right.png')
v_b = Button(image=v_img, highlightthickness=0)
v_b.grid(row= 2, column = 2)

x_img = PhotoImage(file='C:/Users/user/Desktop/flash-card-project-start/images/wrong.png')
x_b = Button(image=x_img, highlightthickness=0)
x_b.grid(row= 2, column = 1)

window.mainloop()