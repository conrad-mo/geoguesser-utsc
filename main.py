import tkinter as tk
from tkinter import *
from tkinter import ttk

# FUNCTIONS


# function to start game when start button pressed
def start_game():
    menu_frame.pack_forget()


# create tkinter object, disable resize
root = Tk()
root.resizable(False, False)

# assign size of root and create a bg variable
root.geometry("532x572")

# main menu frame
menu_frame = Frame(root, height=root.winfo_height(), width=root.winfo_width())
menu_frame.pack(expand=True, fill=BOTH)

# main menu title, and place it at the top
menu_title = Label(menu_frame,
                   text="UTSC Geoguessr",
                   font=("Helvetica", 14))
menu_title.place(relx=0.5, rely=0.03, anchor='center')

# main menu start button:
start_button = Button(
    menu_frame,
    text="Start Playing!",
    command=lambda: menu_frame.pack_forget())
# put button near middle
start_button.place(relx=0.5, rely=0.4, anchor='center')

# main menu quit button:
quit_button = Button(
    menu_frame,
    text="Quit",
    command=lambda: root.quit())
# put button below start button
quit_button.place(relx=0.5, rely=0.5, anchor='center')

# run tkinter
root.mainloop()