from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name Is Joey Smith")
# Shoving it onto the screen

# User can input as many grid please.
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)


root.mainloop()
