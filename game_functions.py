from typing import List
import math

def calculate_score(x: int, y: int, photo_id: int) -> int:
    """Return the score given the coordinates from x, y, and photo_id.
    
    """
    distance = math.sqrt((x - get_photo_coords(photo_id)[0]) ** 2 + (y - 
    get_photo_coords[1]) ** 2)
    
    return round(1000 / distance, 2)


def get_photo_coords(photo_id: int) -> List[int]:
    """
    """
    pass


def get_random_picture(lst: List[int]) -> int:
    """
    """
    pass