from tkinter import *

root = Tk()
root.title("Learning To Code Frame")

# Creating a Label widget../ Also we can remove the #text for a cleaner look.
frame = LabelFrame(
    root, text="...Frame ....", padx=50, pady=60
)  # padx=10, pady=10 padding on the inside.
# padx=10, pady=10 padding for the outside
frame.pack(padx=100, pady=100)

# display onto the screen
b = Button(frame, text="Click Here To Enter...!")
b2 = Button(frame, text="....or Click Here.!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()
