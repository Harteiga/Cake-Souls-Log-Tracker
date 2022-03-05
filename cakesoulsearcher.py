# -*- coding: utf-8 -*-
"""
Created on Thu Mar 3 2022, Version 1.0.1 from Fri Mar 4 2022
@author: Harteiga
"""
import os, gzip, tkinter

def change_path(): # Changes the current directory
    path = tkinter.filedialog.askdirectory(title='Select Logs Folder')
    display.configure(text=f"Current directory is {path}.")
    os.chdir(path)
    
def get_file_list(directory): # Lists files in directory and subdirectories
    file_list = list()
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path): file_list += get_file_list(full_path)
        else: file_list.append(full_path)
    return file_list

def search_path(): # Searches through a directory and updates the results
    cakes_eaten = soul_drops = 0 # Initializes values
    CAKE_TEXT = " thread/INFO]: [CHAT] Yum! You gain +"
    SOUL_TEXT = " thread/INFO]: [CHAT] You found a Cake Soul!"  
    for file in get_file_list("."): # Goes through logs folder
        if file.endswith(".log.gz"): log_text = gzip.open(file, "rb").read()
        elif file.endswith(".log"): log_text = open(file).read()
        else: continue
        cakes_eaten += str(log_text).count(CAKE_TEXT)
        soul_drops += str(log_text).count(SOUL_TEXT)
    count.configure(text=results_text(cakes_eaten, soul_drops))

def results_text(cakes, souls): # Creates the text for results
    return f'The current results are: {cakes} cakes eaten, {souls} cake soul \
drops, which can be submitted as "{cakes-souls} {souls} UPDATED/NEW.".'

def create_window(): # Creates the window
    global display, count
    root = tkinter.Tk() 
    root.title("Cake Souls Log Searching Tool")
    root.geometry("850x100")
    tkinter.Label(root, text="Choose the directory where your logs are kept. \
This is likely %appdata%/.minecraft/logs but may be elsewhere. Supported \
clients are Vanilla and Badlion.").grid(row=1)
    display = tkinter.Label(root, text=f"Current directory is {os.getcwd()}.")
    display.grid(row=2)
    count = tkinter.Label(root, text=results_text(0,0))
    count.grid(row=3)
    buttons = tkinter.Frame(root) # Frame for buttons
    buttons.grid(row=4)
    change = tkinter.Button(buttons, text="Change Directory", \
                    command=lambda: change_path()).grid(row=1, column=1)
    search = tkinter.Button(buttons, text="Search Current Directory", \
                    command=lambda: search_path()).grid(row=1, column=2)
    root.mainloop()
    
create_window()