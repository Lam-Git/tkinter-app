from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learn To Code With Message Box")


# Display to choose from: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
# def popup():
# response = messagebox........"showinfo"---> can be replace with any of the variable


def popup():
    response = messagebox.askquestion("This is my Popup!", "Hello Everyone.....!")
    Label(root, text=response).pack()


# if you un-# the if statements it will display the text message.
# if response == "yes":
# 	Label(root, text="You Clicked Yes!").pack()
# else:
# 	Label(root, text="You Clicked No!!").pack()


Button(root, text="Popup", command=popup).pack()


mainloop()
