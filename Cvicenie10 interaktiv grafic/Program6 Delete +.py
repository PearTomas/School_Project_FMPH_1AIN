'''
Podobne ako v (4) úlohe: klikanie do plochy kreslí '+' a zapamätáva tieto body. Ak mám aspoň 3 zapamätané body
a pritom prvý a posledný majú vzdialenosť menšiu ako 5, ukončí sa zapamätávanie bodov, nakreslí sa z nich náhodne
zafarbený polygon a všetko sa začne od začiatku.

As in task 4: clicking on the area draws a '+' and remembers these points. If I have at least 3 memorized points
and the first and last have a distance of less than 5, the memorization of points is terminated, randomly drawn from them
colored polygon and everything starts from the beginning.
'''

import tkinter
from random import randrange

xy = []

def draw_polygon(event):
    if len(xy) == 0:
        canvas.create_text(event.x, event.y,text="+",fill="red",font="arial 15",tag="plus")
    else:
        canvas.create_text(event.x, event.y, text="+",tag="plus")
    xy.append(event.x)
    xy.append(event.y)

    if len(xy) >= 3 and abs(xy[0]-event.x) <= 10 and abs(xy[1]-event.y) <= 10:
        canvas.create_polygon(xy,fill=f"#{randrange(256**3):06x}")
        xy[:] = []
        canvas.delete("plus")

def delete_canvas(event):
    canvas.delete("all")
    xy[:] = []


canvas = tkinter.Canvas(width="800", height="700")
canvas.pack()

canvas.bind("<ButtonPress-1>", draw_polygon)
canvas.bind("<ButtonPress-3>", delete_canvas)

canvas.mainloop()
