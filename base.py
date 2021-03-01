from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Base Window")


def open():
    global my_img
    top = Toplevel()
    top.title(" Popup Window")
    my_img = ImageTk.PhotoImage(Image.open("images/japan.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="Second Window Open", command=open).pack()


mainloop()

