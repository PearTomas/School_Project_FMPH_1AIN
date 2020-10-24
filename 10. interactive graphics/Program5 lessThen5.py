'''
Vylepši riešenie (5) úlohy: pri kreslení polygónu sa automaticky všetky '+' z plochy vymažú canvas.delete(...).
Každému nakreslenému '+' môžeš pridať rovnaký tag a potom ich naraz zrušíš.

Improves the solution (5) of the task: when drawing a polygon, all '+' are automatically deleted from the surface
canvas.delete (...). You can add the tag to each drawn '+' and then cancel them at once.
'''

import tkinter
from random import randrange

xy = []

def draw_polygon(event):
    if len(xy) == 0:
        canvas.create_text(event.x, event.y, text="+", fill="red", font="arial 15", tag="plus")
    else:
        canvas.create_text(event.x, event.y, text="+", tag="plus")
    xy.append(event.x)
    xy.append(event.y)

    if len(xy) >= 3 and abs(xy[0]-event.x) <= 10 and abs(xy[1]-event.y) <= 10:
        canvas.create_polygon(xy,fill=f"#{randrange(256**3):06x}")
        xy[:] = []

def delete_canvas(event):
    canvas.delete("all")
    xy[:] = []


canvas = tkinter.Canvas(width="800", height="700")
canvas.pack()

canvas.bind("<ButtonPress-1>", draw_polygon)
canvas.bind("<ButtonPress-3>", delete_canvas)

canvas.mainloop()
