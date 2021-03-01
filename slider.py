from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Leveler ")
root.geometry("400x400")
# the app will open and size it up according to the number user choose.

vertical = Scale(root, from_=0, to=500)  # place your Scale number for "Vertical"
vertical.pack()


def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


# place your Scale number for "Horizontal"
vertical.pack()
horizontal = Scale(root, from_=0, to=600, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()


my_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()
