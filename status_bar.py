from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer ")

# Open Image
image1 = Image.open("images/dubai.jpg")
image2 = Image.open("images/iceland.jpg")
image3 = Image.open("images/island.jpg")
image4 = Image.open("images/japan.jpg")
image5 = Image.open("images/vietnam.jpg")

# resizing the images with "height=300, width=225"
resized = image1.resize((300, 225), Image.ANTIALIAS)
resized1 = image2.resize((300, 225), Image.ANTIALIAS)
resized2 = image3.resize((300, 225), Image.ANTIALIAS)
resized3 = image4.resize((300, 225), Image.ANTIALIAS)
resized4 = image5.resize((300, 225), Image.ANTIALIAS)

# take the variable and plug it into the end.
my_img1 = ImageTk.PhotoImage(resized)
my_img2 = ImageTk.PhotoImage(resized1)
my_img3 = ImageTk.PhotoImage(resized2)
my_img4 = ImageTk.PhotoImage(resized3)
my_img5 = ImageTk.PhotoImage(resized4)

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(
    root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E
)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(
        root,
        text="Image " + str(image_number) + " of " + str(len(image_list)),
        bd=1,
        relief=SUNKEN,
        anchor=E,
    )
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number + 1)
    )  # right arrow button to move the img to right.
    button_back = Button(
        root, text="<<", command=lambda: back(image_number - 1)
    )  # left arrow button to move the img to left.

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Update Status Bar
    status = Label(
        root,
        text="Image " + str(image_number) + " of " + str(len(image_list)),
        bd=1,
        relief=SUNKEN,
        anchor=E,
    )

    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()
