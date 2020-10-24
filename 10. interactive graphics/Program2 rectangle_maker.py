'''
Program zabezpečí klikanie myšou: prvé kliknutie si zapamätá súradnice, druhé kliknutie nakreslí
obdĺžnik (create_rectangle), v ktorom jeden vrchol je zapamätaný a druhý vrchol je práve kliknutý.
Obdĺžnik je zafarbený náhodnou farbou.

The program will provide a mouse click: the first click remembers the coordinates, the second click draws
a rectangle (create_rectangle) in which one vertex is memorized and the other vertex is just clicked.
The rectangle is colored a random color.
'''
import tkinter
from random import randrange


xy = [None,None]

def draw_rectangle(event):
    x, y = event.x, event.y
    if xy[0] != None:
        canvas.create_rectangle(xy, x, y,fill=f'#{randrange(256**3):06x}')
        xy[:] = [None, None]
    else:
        xy[:] = [x, y]

def delete_canvas(event):
    canvas.delete('all')
    xy[:] = [None, None]

canvas = tkinter.Canvas(width= "1200", height= "700")
canvas.pack()

canvas.bind("<ButtonPress-1>", draw_rectangle)
canvas.bind("<ButtonPress-3>", delete_canvas)


canvas.mainloop()