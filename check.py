from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Coding Check Box")
root.geometry("400x400")

# this function will show the amount of time its being click
def show():
    myLabel = Label(root, text=var.get()).pack()


# create a variable.. this is an IntVar() meaning number variable
var = IntVar()

c = Checkbutton(root, text="I dare you..check this box. ", variable=var)
c.pack()

# This button will display the --> def show() function
myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
