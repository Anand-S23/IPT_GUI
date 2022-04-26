import pygame
from enum import Enum

# Settings
WIDTH = 640
HEIGHT = 480
FPS = 120
TITLE = "Intune Prep Tool GUI"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
LIGHT_GRAY = (200, 200, 200)
DRAK_GRAY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0);

class Button_State(Enum):
    DEFUALT = 0
    HOVER = 1
    ACTIVE = 3

class Button():
    def __init__(self, dim, color, hover_color, active_color, font, text):
        self.dim = dim
        self.color = color
        self.hover_color = hover_color
        self.active_color = active_color
        self.hover = Button_State.DEFUALT
        self.text = font.render(text, True, BLACK)

    def draw(self, surface):
        if self.hover == Button_State.HOVER:
            pygame.draw.rect(surface, self.hover_color, self.dim)
        elif self.hover == Button_State.ACTIVE:
            pygame.draw.rect(surface, self.active_color, self.dim)
        else:
            pygame.draw.rect(surface, self.color, self.dim)
        
        x_pos = self.dim.center[0] - (self.text.get_width() / 2)
        y_pos = self.dim.center[1] - (self.text.get_height() / 2)
        surface.blit(self.text, (x_pos, y_pos))
