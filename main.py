import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import database as db
import constants as const
import game_functions as gf


# Variables
unused_photos = list(range(len(db.coords)))
time_left = 30
current_photo_id = 0
score = 0
game_round = 0



# FUNCTIONS

# function to reset all game info
def reset_gamestate():
    unused_photos = list(range(len(db.coords)))
    time_left = 30
    current_photo_id = 0
    score = 0
    game_round = 0    


# function to start game when start button pressed
def start_game():
    reset_gamestate()
    next_round()
    #print("ASD")
    game_frame.pack(expand=True, fill=BOTH)
    menu_frame.pack_forget()


# create tkinter object, disable resize
root = Tk()
root.resizable(False, False)

# assign size of root and create a bg variable
root.geometry("1280x720")

# main menu frame
menu_frame = Frame(root, height=root.winfo_height(), width=root.winfo_width(), bg = "#E8F4EA")
menu_frame.pack(expand=True, fill=BOTH),

start_sample= (Image.open('./assets/click_to_start.png'))

background_img = Image.open("./assets/home_page.jpg")
backgroundmenu= background_img.resize((1280,720), Image.ANTIALIAS)
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
    command=lambda: start_game())
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






game_frame = Frame(root, height=root.winfo_height(), width=root.winfo_width())

bgimgfile = Image.open('./assets/game_screen.png')
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
    
    if(game_round != rround):
        return
    
    
    global time_left
    time_left = time_left - 1
    
    if time_left == 0:
        game_end()
    else:
        timer['text'] = time_left
        timer.after(1000, lambda: countdown(rround))
    

def game_end():
    gameover_frame.pack(expand=True, fill=BOTH)
    game_frame.pack_forget()

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
        


def callback(e):
    x= e.x
    y= e.y
    print("Pointer is currently at %d, %d" %(x,y))
    guess(x,y)
map_label.bind('<Button-1>',callback)






# frame for game over screen
gameover_frame = Frame(root, height=root.winfo_height(), width=root.winfo_width())

# set background for game over screen
gameover_image = Image.open('./assets/UTSC_Geo-Guesser.png')
gameover_bg = gameover_image.resize((1200, 700), Image.ANTIALIAS)
gameover_bg = ImageTk.PhotoImage(gameover_bg)

# assign game over image to a label
background_label = Label(gameover_frame, image=gameover_bg)
background_label.pack()

# variable to display final score
final_score = '2'

# create and place label for score
score_label_end = Label(
    gameover_frame,
    height=1,
    width=1,
    text=final_score,
    borderwidth=0,
    foreground='#628060',
    background='white'
    )
score_label_end.place(relx=0.45, rely=0.55, anchor='center')
score_label_end.config(font=("Times New Roman", 50, 'bold'))

# replay button image
replay_button_img = (Image.open('./assets/Play_Again.png'))
replay_icon = replay_button_img.resize((260, 100), Image.ANTIALIAS)
replay_icon = ImageTk.PhotoImage(replay_icon)


# function to replay game
def replay_game():
    gameover_frame.forget()
    # put the code to change to game frame here


# create replay button
replay_button = Button(
    gameover_frame,
    image=replay_icon,
    background='#E8F4EA',
    borderwidth=0,
    command=lambda: replay_game())
replay_button.place(relx=0.45, rely=0.85, anchor='center')







# run tkinter
root.mainloop()
