from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Coding ON/OFF Check Box")
root.geometry("400x400")

# this function will show the amount of time its being click
def show():
    myLabel = Label(root, text=var.get()).pack()


# create a variable.. this is an StringVar() meaning wording variable
var = StringVar()

# on/off button
c = Checkbutton(
    root,
    text="Check this box, to turn it on and off.. ",
    variable=var,
    onvalue="on",
    offvalue="off",
)
c.deselect()  # This will automatically deselect the check box
c.pack()

# This button will display the --> def show() function
myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
