'''
Najprv nakresli kruh so stredom (x0, y0) a polomerom r (napríklad pre r, x0, y0 = 120, 150, 130). Potom každé kliknutie
do vnútra kruhu zmení farbu výplne na odtieň šedej - čím bližšie do stredu tým tmavšie (v strede kruhu čierne),
ku okraju svetlejšie (na obvode biele). Zrejme pri kliknutí vypočítaš vzdialenosť od stredu kruhu a toto číslo potom
prepočítaš na celé číslo od 0 do 255 (napríklad f = int(255 * vzd / r)). Z tohto čísla vyrobíš šedý odtieň
pre farbu kruhu (zrejme rgb(f, f, f)). Nepoužívaj global. Namiesto klikania môžeš otestovať ťahanie myšou.

First, draw a circle with center (x0, y0) and radius r (for example, for r, x0, y0 = 120, 150, 130). Then every click
changes the color of the fill to a shade of gray inside the circle - the closer to the center the darker
(black in the middle of the circle),lighter to the edge (white on the perimeter).
Apparently when you click, you calculate the distance from the center of the circle and then this
number you convert to an integer from 0 to 255 (for example, f = int (255 * vzd / r)). You will make a gray
tint from this number for circle color (probably rgb (f, f, f)). Do not use global. Instead of clicking, you can test
dragging with the mouse.
'''

import tkinter

cir = [200, 300, 300] #r,x,y

def circle1(event):
    x1 = int(abs(event.x - cir[1]))
    y1 = int(abs(event.y - cir[2]))
    r1 = ((x1)**2 + (y1)**2)**0.5
    if r1 <= cir[0]:
        color = int((255 / cir[0])*r1)
        canvas.create_oval(cir[1] - cir[0], cir[2] - cir[0], cir[1] + cir[0], cir[2] + cir[0], fill=f"#{color:02x}{color:02x}{color:02x}")

def delete_canvas(event):
    canvas.delete("all")

canvas = tkinter.Canvas(width= "900", height= "700")
canvas.pack()

canvas.create_oval(cir[1]-cir[0],cir[2]-cir[0],cir[1]+cir[0],cir[2]+cir[0],fill="white")

canvas.bind("<B1-Motion>",circle1)
canvas.bind("<ButtonPress-1>", circle1)
canvas.bind("<ButtonPress-3>", delete_canvas)
canvas.mainloop()