import pygame
import pygame_gui
from tkinter import filedialog as fd
from enum import Enum
from pygame_gui.windows.ui_file_dialog import UIFileDialog
import os
from defs import *

class File_Selection(Enum):
    NONE = 0
    SETUP = 1
    SOURCE = 2
    OUTPUT = 3

def select_dir():
    filepath = fd.askopenfilename()
    print(filepath)

def select_file():
    filepath = fd.askopenfilename()
    print(filepath)

# Point inside rect check
def check_interacting(obj_dim, x, y):
    return (x >= obj_dim.x and x <= obj_dim.x + obj_dim.w and
            y >= obj_dim.y and y <= obj_dim.y + obj_dim.h)

def button_dim(x, y, w=250, h=70):
    return pygame.Rect(x, y, w, h)

def main():
    # Initalize App Context
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial.ttf', 24)
    title_font = pygame.font.SysFont('Arial.ttf', 48)
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))
    running = True
    prev_down = False

    # Create Objects within app
    setup_button  = Button(button_dim(10, 100), font, 'Select Setup Folder', GRAY, LIGHT_GRAY)
    source_button = Button(button_dim(10, 200), font, 'Select Source Setup File', GRAY, LIGHT_GRAY)
    output_button = Button(button_dim(10, 300), font, 'Select Output Folder', GRAY, LIGHT_GRAY)
    submit_button = Button(button_dim(10, 400, 620, 70), font, 'Submit', GREEN, LIGHT_GRAY)

    paths = {
        "setup": "",
        "source": "",
        "output": ""
    }

    title = title_font.render(TITLE, True, BLACK)
    setup_text = font.render("''", True, BLACK)
    source_text = font.render("''", True, BLACK)
    output_text = font.render("''", True, BLACK)

    file_selection_type = File_Selection.NONE

    while running:
        time_delta = clock.tick(FPS) / 1000.0

        # Get inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == file_selection.ok_button:
                    if file_selection_type == File_Selection.SETUP:
                        paths["setup"] = file_selection.current_file_path
                        setup_text = font.render(f"'{file_selection.current_file_path}'", True, BLACK)

                    elif file_selection_type == File_Selection.SOURCE:
                        paths["source"] = file_selection.current_file_path
                        source_text = font.render(f"'{file_selection.current_file_path}'", True, BLACK)

                    elif file_selection_type == File_Selection.OUTPUT:
                        paths["output"] = file_selection.current_file_path
                        output_text = font.render(f"'{file_selection.current_file_path}'", True, BLACK)

                    print(file_selection.current_file_path)

            manager.process_events(event)

        left_down, _, right_down = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Update application
        setup_button.hover = check_interacting(setup_button.dim, mouse_x, mouse_y)
        source_button.hover = check_interacting(source_button.dim, mouse_x, mouse_y)
        output_button.hover = check_interacting(output_button.dim, mouse_x, mouse_y)
        submit_button.hover = check_interacting(submit_button.dim, mouse_x, mouse_y)

        if left_down and not prev_down:
            if setup_button.hover:
                """
                file_selection_type = File_Selection.SETUP
                file_selection = UIFileDialog(rect=pygame.Rect(0, 0, 300, 300), manager=manager, allow_picking_directories=True)
                print(file_selection.current_file_path)
                """
                select_dir()

            elif source_button.hover: 
                file_selection_type = File_Selection.SOURCE
                file_selection = UIFileDialog(rect=pygame.Rect(0, 0, 300, 300), manager=manager, allow_picking_directories=True)
                print(file_selection.current_file_path)

            elif output_button.hover: 
                file_selection_type = File_Selection.OUTPUT
                file_selection = UIFileDialog(rect=pygame.Rect(0, 0, 300, 300), manager=manager, allow_picking_directories=True)
                print(file_selection.current_file_path)

            elif submit_button.hover: 
                file_selection = UIFileDialog(rect=pygame.Rect(0, 0, 300, 300), manager=manager, allow_picking_directories=True)

        prev_down = left_down
        manager.update(time_delta)

        # Render applications
        screen.fill(WHITE)

        # Render Text
        screen.blit(title, (0, 0))
        screen.blit(setup_text, (280, 125))
        screen.blit(source_text, (280, 225))
        screen.blit(output_text, (280, 325))

        # Render Buttons
        setup_button.draw(screen)
        source_button.draw(screen)
        output_button.draw(screen)
        submit_button.draw(screen)

        manager.draw_ui(screen)
        pygame.display.flip()

if __name__ == '__main__':
    # Initialize application
    pygame.init()
    pygame.font.init()

    main()
    pygame.quit()

