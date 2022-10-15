import tkinter as tk
from tkinter import *
from tkinter import ttk

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
    text="Start Playing!")
start_button.place(relx=0.5, rely=0.1, anchor='center')

# main menu quit button:
quit_button = Button(
    menu_frame,
    text="Quit")
quit_button.place(relx=0.5, rely=0.175, anchor='center')

# run tkinter
root.mainloop()
