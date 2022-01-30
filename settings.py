import pygame
import os

"""
Initializing Global Variables
"""

# Flags
control_screen_flag = 0

# Defining width and height of the screen
WIDTH = 800
HEIGHT = 600

# Setting button width and height
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40

# Setting the speed of the game
FPS = 60

# defining colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0,255,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (193,205,205)

# Creating a vector
vec = pygame.math.Vector2

# Font
font_name = pygame.font.match_font('arial')

# Making main directory path
main_path = os.path.dirname(__file__)

# Making image directory path
image_path = os.path.join(main_path, "images")

# Making map directory path
maps_path = os.path.join(image_path, "maps")

# Making preview directory path
previews = os.path.join(image_path, "map_preview")

# Making keyboard keys directory path
keys = os.path.join(image_path, "keyboard_keys")