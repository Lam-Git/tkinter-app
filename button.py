from tkinter import *

root = Tk()

# creating the button to click
def myClick():
    myLabel = Label(root, text="Click me..! ")
    myLabel.pack()


# Creating a Buttonwidget
myButton = Button(root, text="Send Here..!")  # widget
# change the size of button "pady" and "padx" at the end of the widget...(root, text="Send Here..!", pady=50, padx=50)

# Shoving it onto the screen
myButton.pack()

root.mainloop()
