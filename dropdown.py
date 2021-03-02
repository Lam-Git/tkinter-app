from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Coding a Drop Box...!")
root.geometry("400x400")


def show():
    myLabel = Label(root, text=clicked.get()).pack()


# MUST have the variable
clicked = StringVar()
clicked.set("Monday")
# Must create a drop funcation.. OptionMenu(root, anything you want in this box)
drop = OptionMenu(
    root,
    clicked,
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thurday",
    "Friday",
    "Saturday",
    "Sunday",
)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()
root.mainloop()
