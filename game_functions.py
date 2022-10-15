from typing import List
import math
import database as DB
import random

def calculate_score(x: int, y: int, photo_id: int) -> int:
    """Return the score given the coordinates from x, y, and photo_id.
    
    """
    distance = math.sqrt((x - get_photo_coords(photo_id)[0]) ** 2 + (y - 
    get_photo_coords[1]) ** 2)
    
    return round(1000 / distance, 2)


def get_photo_coords(photo_id: int) -> List[int]:
    """Return the coordinates of the photo given index photo_id
        
    """
    return DB.coords [photo_id]


def get_random_picture(lst: List[int]) -> int:
    """Return a random coordinate from the list lst and then 
       removes it from lst

    """
    
    random_num = random.choice(lst)
    lst.remove(random_num)
    return random_num
  
    
