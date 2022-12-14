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

# create and place label for score
score_label = Label(
    gameover_frame,
    height=1,
    width=1,
    text=final_score,
    borderwidth=0,
    foreground='#628060',
    background='white'
    )
score_label.place(relx=0.45, rely=0.55, anchor='center')
score_label.config(font=("Times New Roman", 50, 'bold'))

# replay button image
replay_button_img = (Image.open('./assets/Play_Again.png'))
replay_icon = replay_button_img.resize((260, 100), Image.ANTIALIAS)
replay_icon = ImageTk.PhotoImage(replay_icon)


# function to replay game
def replay_game():
    gameover_frame.forget()
    # put the code to change to game frame here


# create replay button
replay_button = Button(
    gameover_frame,
    image=replay_icon,
    background='#E8F4EA',
    borderwidth=0,
    command=lambda: replay_game())
replay_button.place(relx=0.45, rely=0.85, anchor='center')

root.mainloop()
