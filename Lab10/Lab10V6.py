import itertools
from tkinter import *

root = Tk()
root.title("Лабораторна робота №10")
root.geometry("800x500")
canvas = Canvas(root, width=800, height=500, bg='white')
color_iteration = itertools.cycle(('green', 'yellow', 'blue', 'black', 'lime'))


def move():
    global direction
    if canvas.coords(circle)[0] >= 700 or canvas.coords(circle)[0] <= 0:
        direction = -direction
    if canvas.coords(circle)[0] == 150 or canvas.coords(circle)[0] == 350\
            or canvas.coords(circle)[0] == 475 or canvas.coords(circle)[0] == 650:
        canvas.itemconfig(circle, fill=next(color_iteration), outline=next(color_iteration))
    canvas.move(circle, direction, 0)
    root.after(10, move)


btn_move = Button(text="Перемістити", command=move)
btn_move.pack()
canvas.pack()

direction = 5
circle = canvas.create_oval(10, 10, 60, 60, fill=next(color_iteration), outline=next(color_iteration))

root.mainloop()
