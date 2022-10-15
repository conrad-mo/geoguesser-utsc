import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

# FUNCTIONS


# function to start game when start button pressed
def start_game():
    menu_frame.pack_forget()


# create tkinter object, disable resize
root = Tk()
root.resizable(False, False)

# assign size of root and create a bg variable
root.geometry("1200x700")

# main menu frame
menu_frame = Frame(root, height=root.winfo_height(), width=root.winfo_width(), bg = "#E8F4EA")
menu_frame.pack(expand=True, fill=BOTH),

start_sample= (Image.open('./assets/click_to_start.png'))

background_img = Image.open("./assets/home_page.jpg")
backgroundmenu= background_img.resize((1200,700), Image.ANTIALIAS)
backgroundmenu= ImageTk.PhotoImage(backgroundmenu)

# Create a Label Widget to display the text or Image
label = Label(menu_frame, image = backgroundmenu)
label.pack()
# main menu start button:
start_sample= (Image.open('./assets/click_to_start.png'))
start_icon= start_sample.resize((259, 75), Image.ANTIALIAS)
start_icon= ImageTk.PhotoImage(start_icon)
start_button = Button(
    menu_frame,
    image=start_icon,
    bg = "#E8F4EA",
    command=lambda: menu_frame.pack_forget())
start_button.pack(pady = 20)
# put start button near middle
start_button.place(relx=0.139, rely=0.62, anchor='center')

# how to play button
how_to_sample= (Image.open('./assets/how_to_play.png'))
how_to_icon= how_to_sample.resize((259, 75), Image.ANTIALIAS)
how_to_icon= ImageTk.PhotoImage(how_to_icon)
how_to_button = Button(
    menu_frame,
    image=how_to_icon,
    bg = "#E8F4EA",
    command=lambda: menu_frame.pack_forget()) #Change this later
how_to_button.pack(pady = 20)

# put how to play button near middle
how_to_button.place(relx=0.37, rely=0.62, anchor='center')

# main menu quit button:
quit_button = Button(
    menu_frame,
    text="Quit",
    command=lambda: root.quit())
# put button below start button
quit_button.place(relx=0.5, rely=0.5, anchor='center')

# run tkinter
root.mainloop()