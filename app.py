import os
import tkinter as tk
from tkinter import filedialog as fd

paths = {
    "setup": "",
    "source": "",
    "output": ""
}

def submit():
    pass

def select_file(key, widget, is_directory=True):
    if is_directory:
        filename = fd.askdirectory()
    else:
        filename = fd.askopenfilename()

    if filename:
        paths[key] = filename
        new_label = f"'{filename}'"
        widget.config(text=new_label)
        print(paths[key])

def init_app():
    window = tk.Tk()
    window.geometry("640x480")
    window.title('Intune Prep Tool GUI')
    return window

def main():
    window = init_app()
    app_font = ('Arial', 18, 'bold')
    path_font = ('Arial', 14)
    title_width = 300

    # Title
    title_x = (640 - title_width) / 2
    title = tk.Label(window, text='Intune Prep Tool GUI', font=app_font)  
    title.place(x=title_x, y=0)

    # Setup Row
    setup = tk.Button(window, text='Select Setup Folder', width=67, command=lambda:select_file("setup", setup))
    setup.place(x=5, y=50)

    # Source Row
    source = tk.Button(window, text='Select Source File', width=66, command=lambda:select_file("source", source, False))
    source.place(x=5, y=100)

    # Output Row
    output = tk.Button(window, text='Select Ouput Folder', width=65, command=lambda:select_file("output", output))
    output.place(x=5, y=150)

    # Submit Button
    output = tk.Button(window, text='Submit', width=64, command=lambda:submit())
    output.place(x=5, y=200)

    # Update App
    window.mainloop()


if __name__ == '__main__':
    main()

