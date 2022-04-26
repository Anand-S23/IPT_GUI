import os
import tkinter as tk
from tkinter import filedialog as fd

paths = {
    "setup": "",
    "source": "",
    "output": ""
}

def reset(setup, source, output, result):
    paths["setup"] = ""
    paths["source"] = ""
    paths["ouput"] = ""

    setup.config(text="Select Setup Folder")
    source.config(text="Select Source File")
    output.config(text="Select Ouput Folder")
    result.config(text="Success!")

def submit(setup, source, output, result):
    # Check if there is issue with paths
    if paths["setup"] == "" or paths["source"] == "" or paths["output"] == "":
        result.config(text="One of the inputs are missing, fill to continue")
        return

    os.system(f"IntuneWinAppUtil -c {paths['setup']} -s {paths['source']} -o {paths['output']}")
    reset(setup, source, output, result)

def select_file(key, widget, is_directory=True):
    if is_directory:
        filename = fd.askdirectory()
    else:
        filename = fd.askopenfilename()

    if filename:
        paths[key] = filename
        new_label = f"'{filename}'"
        widget.config(text=new_label)

def init_app():
    window = tk.Tk()
    window.geometry("640x300")
    window.title('Intune Prep Tool GUI')
    return window

def main():
    window = init_app()
    app_font = ('Arial', 18, 'bold')
    result_font = ('Arial', 14)
    title_width = 300

    # Title
    title_x = (640 - title_width) / 2
    title = tk.Label(window, text='Intune Prep Tool GUI', font=app_font)  
    title.place(x=8, y=0)

    # Result
    result = tk.Label(window, text='', font=result_font)  
    result.place(x=8, y=250)

    # Setup Row
    setup = tk.Button(window, text='Select Setup Folder', width=88, command=lambda:select_file("setup", setup))
    setup.place(x=8, y=50)

    # Source Row
    source = tk.Button(window, text='Select Source File', width=88, command=lambda:select_file("source", source, False))
    source.place(x=8, y=100)

    # Output Row
    output = tk.Button(window, text='Select Ouput Folder', width=88, command=lambda:select_file("output", output))
    output.place(x=8, y=150)

    # Submit Button
    submit_btn = tk.Button(window, text='Submit', width=88, command=lambda:submit(setup, source, output, result))
    submit_btn.place(x=8, y=200)

    # Update App
    window.mainloop()


if __name__ == '__main__':
    main()

