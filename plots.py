from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

# Intall pip package:
# pip install numpy
# pip install matplotlib

root = Tk()
root.title("Learning to Code with Matplotlibs ")
root.geometry("400x200")


def graph():
    house_princes = np.random.normal(200000, 250000, 150500)
    plt.hist(house_princes, 150)
    plt.show()


my_button = Button(root, text="Graphing this Graph", command=graph)
my_button.pack()

root.mainloop()
