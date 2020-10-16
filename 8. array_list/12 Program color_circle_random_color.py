'''
Napíš funkciu nahodne_farby(n), ktorá vygeneruje a vráti n-prvkový zoznam náhodných farieb.
Tento zoznam môžeme poslať do funkcie kresli z predchádzajúcej úlohy.

Write a function random_colors (n) that generates and returns an n-element list of random colors.
We can use the draw(r,list) function from the previous task(11 Program color_circle).
'''


def draw(r,list):
    x = 10 + r
    y = 100 - r
    for l in list:
        color = l
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=color)
        x += r*2

def random_color(n):
    color = []
    for i in range(n):
        color.append(f'#{randrange(256 ** 3):06x}')
    return color




import tkinter
from random import randrange

canvas = tkinter.Canvas(height = "200",width = "500" )
canvas.pack()

draw(9, random_color(20))

tkinter.mainloop()