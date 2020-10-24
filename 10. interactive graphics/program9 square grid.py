'''
Predstav si, že celá grafická plocha je štvorcová sieť, ktorej štvorčeky majú veľkosť 50x50. Napíš program,
ktorý pri každom kliknutí do grafickej plochy nakreslí náhodne zafarbený príslušný štvorček tejto siete
pomocou create_rectangle(). Nepoužívaj global.

Imagine that the whole graphics area is a square grid, the squares of which are 50x50. Write a program
which, each time you click into the graphics area, draws a randomly colored corresponding square of that grid
using create_rectangle (). Do not use global.
'''
from random import randrange
import tkinter
xy = [0,0] # velkost gridu


xy[0] = int(input("grid size for x: "))
xy[1] = int(input("grid size for y: "))

def fill_grid(x,y):
    canvas.create_rectangle(x*xy[0],y*xy[1],(x*xy[0])+xy[0],(y*xy[1])+xy[1],fill=f"#{randrange(256**3):06x}",outline="")

def pos_in_grid(event):
    fill_grid(event.x // xy[0],event.y // xy[1])

def delete_canvas(event):
    canvas.delete("all")


canvas = tkinter.Canvas(width= "900", height= "700")
canvas.pack()

canvas.bind("<B1-Motion>",pos_in_grid)
canvas.bind("<ButtonPress-1>", pos_in_grid)
canvas.bind("<ButtonPress-3>", delete_canvas)
canvas.mainloop()