import tkinter as tk
import random
def update():
    l.config(text=str(random.random()))
    root.after(40, update)
root = tk.Tk()
l = tk.Label(text='9000000000000000009')
l.pack()
root.after(1000, update)
root.mainloop()