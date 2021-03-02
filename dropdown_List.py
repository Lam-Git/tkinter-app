from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Coding a Drop Box...!")
root.geometry("400x400")


def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# MUST have the variable
clicked = StringVar()
clicked.set(
    "Monday"
)  # or you can sub it with (options[1])-->calling the function with the index
# Must create a drop funcation.. OptionMenu(root, anything you want in this box)
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()
root.mainloop()
