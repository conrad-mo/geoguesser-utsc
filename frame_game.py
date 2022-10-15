import tkinter as tk
from tkinter import *
from tkinter import ttk
import game_functions as gf

unused_photos = [0,1,2]

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
    """Decrease time_left by 1. Then, call function lose() if time_left is 0. 
    Else, update timer text and call countdown after 1 second.
    
    """
    global time_left
    time_left = time_left - 1
    
    if time_left == 0:
        lose()
    else:
        timer['text'] = time_left
        timer.after(1000, countdown)    
    

def lose():
    pass

def guess(x: int, y: int):
    """Update score given the guessed coordinates x and y.
    
    """
    
    global score
    global current_photo_id
    
    score += calculate_score(x, y, current_photo_id)


def next_round():
    """Update current_photo_id to a random unused photo and reset time_left to 
    30.
    """
    global current_photo_id
    global unused_photos
    global time_left
    
    current_photo_id = get_random_picture(unused_photos)
    time_left = 30

#start countdown
timer.after(1000, countdown)

# assign size of root and create a bg variable
root.geometry("532x572")

root.mainloop()


# countdown()