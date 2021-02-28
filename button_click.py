from tkinter import *

root = Tk()

# creating the button to click with a function
def myClick():
    myLabel = Label(root, text="Hello its working....! ")
    myLabel.pack()


# Creating a Buttonwidget & must have the "command" in order to active the button.
# fg "forground-color" at the end of command to change text color
# bg "background-color" change the background
myButton = Button(root, text="Send Here..!", command=myClick, fg="red", bg="black")


# Shoving it onto the screen
myButton.pack()

root.mainloop()
