# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:46:46 2022

@author: Harteiga
"""
import os
import gzip
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory

def updateDirectory(): # Updates the current directory
    global path
    path = askdirectory(title='Select Folder')
    display.configure(text=f"Current directory is {path}")
    os.chdir(path)
    
def getListOfFiles(dirName): # Function by Varum for searching directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

def searchDirectory(): # Searches through a directory and updates the results
    cakes_eaten = soul_drops = 0 # Initializes values
    cake_text = " thread/INFO]: [CHAT] Yum! You gain +"
    soul_text = " thread/INFO]: [CHAT] You found a Cake Soul!"  
    for file in getListOfFiles(path): #Goes through logs folder
        if file.endswith(".log.gz"): #Goes through .gz logs
            current_file = gzip.open(file, "rb")
            current_text = current_file.read()
            cakes_eaten += str(current_text).count(cake_text)
            soul_drops += str(current_text).count(soul_text)
        elif file.endswith(".log"): #Goes through uncompressed logs
            current_file = open(file)
            current_text = current_file.read()
            cakes_eaten += current_text.count(cake_text)
            soul_drops += str(current_text).count(soul_text)
        results.configure(text=f'The current results are: {cakes_eaten} cakes eaten, {soul_drops} cake soul drops, which can be submitted as "{cakes_eaten-soul_drops} {soul_drops} UPDATED.".')

path = os.getcwd() # Finds Current Path

frame = Tk() # Creates Window
frame.title("Cake Souls Log Searching Tool")
frame.geometry("750x150")

Label(frame, text="Choose the directory where your logs are kept. This should be %appdata%/.minecraft/logs but may be elsewhere.").grid(row=1, column=1)
Label(frame, text="Known supported clients are Default and Badlion. Likely to support other clients but not guaranteed.").grid(row=2, column=1)
display = Label(frame, text=f"Current directory is {path}")
display.grid(row=3, column=1)
Button(frame, text="Change Directory", command=lambda: updateDirectory()).grid(row=5, column=1)
Button(frame, text="Search Current Directory (May take some time)", command=lambda: searchDirectory()).grid(row=6, column=1)

results = Label(frame, text=f'The current results are: 0 cakes eaten, 0 cake soul drops, which can be submitted as "0 0 UPDATED".')
results.grid(row=4, column=1)

frame.mainloop()


