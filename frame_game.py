import tkinter as tk
from tkinter import *
from tkinter import ttk

time_left = 30


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
    timer['text'] = time_left
    timer.after(1000, countdown)

#start countdown
timer.after(1000, countdown)

# assign size of root and create a bg variable
root.geometry("532x572")

root.mainloop()