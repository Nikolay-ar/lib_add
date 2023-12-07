from tkinter import *
from PIL import ImageTk, Image

root = Tk()
img = ImageTk.PhotoImage(Image.open("1.bmp"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()