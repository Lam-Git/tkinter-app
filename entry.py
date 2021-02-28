from tkinter import *

root = Tk()

e = Entry(root)
# User can ---add e = Entry(root, width=30, bg="blue", fg = "white", boarderwidth=40)
e.pack()


def myClick():
    myLabel = Label(root, text="Dreams coming true! " + e.get())
    myLabel.pack()


# "e.get()" User input will appear along with the "text"

myButton = Button(root, text="Enter Your Name!", command=myClick)
myButton.pack()

root.mainloop()
