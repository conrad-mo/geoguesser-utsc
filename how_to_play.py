import tkinter as tk
from PIL import Image,ImageTk

window = tk.Tk()

bgimgfile = Image.open('./assets/game_instructions.png')
bgimgfile = bgimgfile.resize((1280, 720))

bgimg = ImageTk.PhotoImage(bgimgfile)
lablebgimg = tk.Label(window, image=bgimg)
lablebgimg.pack()



window.mainloop()

