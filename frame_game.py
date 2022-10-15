import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
import game_functions as gf
import database as db
import constants as const
from PIL import Image,ImageTk


unused_photos = list(range(len(db.coords)))

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

bgimgfile = Image.open('./assets/Game_Screen.png')
bgimgfile = bgimgfile.resize((1280, 720))

bgimg = ImageTk.PhotoImage(bgimgfile)
lablebgimg = Label(game_frame, image=bgimg)
lablebgimg.pack()

# timer text, at the top
timer = Label(game_frame,
                   text=time_left,
                   font=("Helvetica", 14))
timer.place(relx=0.5, rely=0.03, anchor='center')
# timer text, at the top
score_label = Label(game_frame,
                   text=current_photo_id,
                   font=("Helvetica", 14))
score_label.place(relx=0.5, rely=0.8, anchor='s')


# Create an object of tkinter ImageTk
img_file = Image.open("./assets/map.jpg")

img_file = img_file.resize((600,600))
img_file = img_file.rotate(-90)
img_file = img_file.resize((675,900))

img = ImageTk.PhotoImage(img_file)

# Create a Label Widget to display the text or Image
photo_label = Label(game_frame, image = img)
photo_label.place(relx=0.015, rely=0.5, anchor='w')



imgmapfile = Image.open("./assets/map.jpg")
imgmapfile = imgmapfile.resize((450, 670))

img_map = ImageTk.PhotoImage(imgmapfile)
map_label = Label(game_frame, image = img_map)
map_label.place(relx=0.995, rely=0.5, anchor='e')



#countdown function
def countdown(rround: int):
    """Decrease time_left by 1. Then, call function game_end() if time_left is 0.
    Else, update timer text and call countdown after 1 second.
    
    """
    global game_round
    
    if(game_round > rround):
        return
    
    
    global time_left
    time_left = time_left - 1
    
    if time_left == 0:
        game_end()
    else:
        timer['text'] = time_left
        timer.after(1000, lambda: countdown(rround))
    

def game_end():
    pass

def guess(x: int, y: int):
    """Update score given the guessed coordinates x and y.
    Then call next round.img2 = ImageTk.PhotoImage(Image.open(path2))
    panel.configure(image=img2)
    panel.image = img2
    """
    global score
    global current_photo_id
    
    score += gf.calculate_score(x, y, current_photo_id)

    imgpointfile = Image.open("./assets/point.png")
    imgpointfile = imgpointfile.resize((25, 25))
    
    img_point = ImageTk.PhotoImage(imgpointfile)
    point_label = Label(map_label, image = img_point)
    point_label.place(relx=x/450, rely=y/670, anchor='center')

    imggoalfile = Image.open("./assets/goal.png")
    imggoalfile = imggoalfile.resize((25, 25))
    
    img_goal = ImageTk.PhotoImage(imggoalfile)
    goal_label = Label(map_label, image = img_goal)
    goal_label.place(relx = gf.get_photo_coords(current_photo_id)[0]/450, rely = gf.get_photo_coords(current_photo_id)[1]/670, anchor='center')    
    
    
    point_label.after(1000, lambda: goal_label.destroy())
    point_label.after(1000, lambda: point_label.destroy())

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
        score_label['text'] = score
        
        # Create an object of tkinter ImageTk
        img_file2 = Image.open("./assets/Photos/" + str(current_photo_id) + ".jpg")
        
        img_file2 = img_file2.resize((600,600))
        img_file2 = img_file2.rotate(-90)
        img_file2 = img_file2.resize((480,640))
        
        img2 = ImageTk.PhotoImage(img_file2)
        photo_label.configure(image=img2)
        photo_label.image = img2
        
        time_left = 30
        
        countdown(game_round)
        

#start countdown
#start first round
next_round()

def callback(e):
    x= e.x
    y= e.y
    print("Pointer is currently at %d, %d" %(x,y))
    guess(x,y)
map_label.bind('<Button-1>',callback)

# assign size of root and create a bg variable
root.geometry("1280x720")

root.mainloop()


# countdown()