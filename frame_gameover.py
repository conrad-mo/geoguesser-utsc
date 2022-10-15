import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# general tkinter object
root = Tk()
root.resizable(False, False)

# assign size of root and create a bg variable
root.geometry("1200x700")

# frame for game over screen
gameover_frame = Frame(root, height=root.winfo_height(), width=root.winfo_width())
gameover_frame.pack(expand=True, fill=BOTH)

# set background for game over screen
gameover_image = Image.open('./assets/UTSC_Geo-Guesser.png')
gameover_bg = gameover_image.resize((1200, 700), Image.ANTIALIAS)
gameover_bg = ImageTk.PhotoImage(gameover_bg)

# assign game over image to a label
background_label = Label(gameover_frame, image=gameover_bg)
background_label.pack()

# variable to display final score
final_score = '2'

# create and place textbox
score_textbox = Label(
    gameover_frame,
    height=1,
    width=1,
    text=final_score,
    borderwidth=0,
    background='white'
    )
score_textbox.place(relx=0.45, rely=0.55, anchor='center')
score_textbox.config(font=("Times New Roman", 50, 'bold'))

# replay button image
replay_button_img = (Image.open('./assets/Play_Again.png'))
replay_icon = replay_button_img.resize((230, 100), Image.ANTIALIAS)
replay_icon = ImageTk.PhotoImage(replay_icon)

# create replay button
replay_button = Button(
    gameover_frame,
    image=replay_icon,
    command=lambda: gameover_frame.forget())
replay_button.place(relx=0.5, rely=0.8, anchor='center')

root.mainloop()
