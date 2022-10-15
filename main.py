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
menu_frame = Frame(root, height=root.winfo_height(), width=root.winfo_width())
menu_frame.pack(expand=True, fill=BOTH)

start_sample= (Image.open('./assets/click_to_start.png'))

background_img = Image.open("./assets/home_page.jpg")
backgroundmenu= background_img.resize((1200,700), Image.ANTIALIAS)
backgroundmenu= ImageTk.PhotoImage(backgroundmenu)

# Create a Label Widget to display the text or Image
label = Label(menu_frame, image = backgroundmenu)
label.pack()
# main menu start button:
start_sample= (Image.open('./assets/click_to_start.png'))
start_icon= start_sample.resize((230,100), Image.ANTIALIAS)
start_icon= ImageTk.PhotoImage(start_icon)
start_button = Button(
    menu_frame,
    image=start_icon,
    command=lambda: menu_frame.pack_forget())
# put button near middle
start_button.place(relx=0.12, rely=0.5, anchor='center')

# main menu quit button:
quit_button = Button(
    menu_frame,
    text="Quit",
    command=lambda: root.quit())
# put button below start button
quit_button.place(relx=0.5, rely=0.5, anchor='center')

# run tkinter
root.mainloop()