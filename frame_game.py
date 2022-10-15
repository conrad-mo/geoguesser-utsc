import tkinter as tk
from tkinter import *
from tkinter import ttk
import game_functions as gf


time_left = 30
current_photo_id = 0
score = 0

# create tkinter object, disable resize
root = Tk()
root.resizable(False, False)

# game frame
game_frame = Frame(root, height=root.winfo_height(), width=root.winfo_width())
game_frame.pack(expand=True, fill=BOTH)

# timer text, at the top
timer = Label(game_frame,
                   text=time_left,
                   font=("Helvetica", 14))
timer.place(relx=0.5, rely=0.03, anchor='center')

#countdown function
def countdown():
    global time_left
    time_left = time_left - 1
    
    #if the timer hits 0, call lose()
    
    
    
    #
    
    timer['text'] = time_left
    timer.after(1000, countdown)

def lose():
    pass

def guess(x: int, y: int):
    #add to score depending on the guess, use current_photo_id as global
    pass

#start countdown
timer.after(1000, countdown)

# assign size of root and create a bg variable
root.geometry("532x572")

root.mainloop()


# countdown()