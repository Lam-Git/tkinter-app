Tkinter is the fastest and easiest way to create the Graphic User Interfaces (GUI applications) with Python. Tkinter comes with Python already, so there's nothing to install!

The basic blueprint of Tkinter:
'''
from tkinter import \*

root = Tk()

# Creating a Label widget

myLabel = Label(root, text="Hello World, I am learning Tkinter!") # widget

# Shoving it onto the screen

myLabel.pack()

root.mainloop()
'''
