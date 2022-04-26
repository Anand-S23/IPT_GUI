import pygame
import os
from defs import *

# Point inside rect check
def check_interacting(obj_dim, x, y):
    return (x >= obj_dim.x and x <= obj_dim.x + obj_dim.w and
            y >= obj_dim.y and y <= obj_dim.y + obj_dim.h)

def main():
    # Initalize App Context
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial.ttf', 32)
    title_font = pygame.font.SysFont('Arial.ttf', 128)
    running = True
    prev_down = False

    # Create Objects within app
    submit_button = Button(pygame.Rect(80, 360, 200, 80), GREEN, GRAY, DRAK_GRAY, font, 'Submit')
    #clear_button = Button(pygame.Rect(360, 360, 200, 80), (255, 0,  0), (150, 150, 150), font, 'Clear')

    #output = font.render('Output:', True, BLACK)

    while running:
        clock.tick(FPS)

        # Get inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        left_down, _, right_down = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Update application
        submit_button.hover = Button_State(check_interacting(submit_button.dim, mouse_x, mouse_y))

        if left_down:
            if submit_button.hover: 
                submit_button.hover = Button_State.ACTIVE

                if not prev_down:
                    # TODO submit
                    pass
                
        prev_down = left_down

        # Render applications
        submit_button.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Initialize application
    pygame.init()
    pygame.font.init()

    main()
    pygame.quit()
