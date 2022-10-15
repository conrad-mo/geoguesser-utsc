import tkinter as tk
from tkinter import *
from tkinter import ttk
import game_functions as gf
import database as db
import constants as const

unused_photos = list(range(len(db.coords)))
print(unused_photos)

time_left = 30
current_photo_id = 0
score = 0
game_round = 0

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
# timer text, at the top
photo_id_label = Label(game_frame,
                   text=current_photo_id,
                   font=("Helvetica", 14))
photo_id_label.place(relx=0.5, rely=0.1, anchor='center')

#countdown function
def countdown():
    """Decrease time_left by 1. Then, call function game_end() if time_left is 0. 
    Else, update timer text and call countdown after 1 second.
    
    """
    global time_left
    time_left = time_left - 1
    
    if time_left == 0:
        game_end()
    else:
        timer['text'] = time_left
        timer.after(1000, countdown)    
    

def game_end():
    pass

def guess(x: int, y: int):
    """Update score given the guessed coordinates x and y.
    Then call next round.
    """
    global score
    global current_photo_id
    
    score += calculate_score(x, y, current_photo_id)
    next_round()

def next_round():
    """Update current_photo_id to a random unused photo and
    reset time_left to 30.
    """
    global current_photo_id
    global unused_photos
    global time_left
    global game_round
    
    game_round += 1
    if(game_round > const.MAX_ROUND):
        game_end()
    else:
        current_photo_id = gf.get_random_picture(unused_photos)
        photo_id_label['text'] = current_photo_id
        time_left = 30

#start countdown
timer.after(1000, countdown)
#start first round
next_round()

# assign size of root and create a bg variable
root.geometry("532x572")

root.mainloop()


# countdown()