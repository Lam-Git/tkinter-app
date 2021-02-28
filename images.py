from tkinter import *
from PIL import ImageTk, Image

# in terminal run ---> pip install Pillow

root = Tk()
root.title("Learning how to code")


my_img = ImageTk.PhotoImage(Image.open("images/japan.jpg"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()

