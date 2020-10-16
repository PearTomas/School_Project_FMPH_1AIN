'''
apíš funkciu kresli(r, zoznam), ktorá z daného zoznamu farieb nakreslí rad farebných kruhov, Každý kruh má polomer r.
Funkcia nemodifikuje vstupný zoznam.

write a function draw(r, list), which draws a series of colored circles from the given list of colors.
Each circle has a radius r. The function doesn't modify the input list.
'''

def draw(r,list):
    x = 10 + r
    y = 100 - r
    for l in list:
        color = l
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=color)
        x += r*2





import tkinter

canvas = tkinter.Canvas(height = "200")
canvas.pack()

draw(20, ['red', 'red', 'blue', 'orange', 'green', 'yellow'])

tkinter.mainloop()