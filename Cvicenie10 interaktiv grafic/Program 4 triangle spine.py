'''
Podobne ako v (3) úlohe: pri každom kliknutí sa na danej pozícii nakreslí '+' (create_text), pritom pri prvých dvoch
kliknutiach sa tieto body zapamätajú. Tretie z týchto troch kliknutí nakreslí náhodne zafarnený trojhuholník
(create_polygon). Zoznam zapamätaných bodov má momentálne 3 vrcholy. Teraz sa z tohto zapamätaného zoznamu
vyhodí prvý prvok a pokračuje sa ďalej s dvomi vrcholmi: ďalšie kliknutie pridá do zoznamu 3. vrchol, nakreslí
trojuholník a prvý vrchol sa opäť vyhodí.

As in (3) task: each time you click, a '+' (create_text) is drawn at the given position, while for the first two
clicks will remember these points. The third of these three clicks draws a randomly colored triangle
(create_polygon). The list of memorized points currently has 3 vertices. Now get off this memorable list
throws the first element and continues with two vertices: the next click adds the 3rd vertex to the list, draws
the triangle and the first vertex are discarded again.
'''
import tkinter
from random import randrange

xy = [None,None,None,None,None,None]

def draw_polygon(event):
    canvas.create_text(event.x,event.y,text="+")
    if xy[1] == None:
        xy[0], xy[1] = event.x, event.y
    elif xy[3] == None:
        xy[2],xy[3] = event.x, event.y
    elif xy[4] == None:
        xy[4], xy[5] = event.x,event.y
        canvas.create_polygon(xy,fill=f'#{randrange(256**3):06x}')
        xy.remove(xy[0])
        xy.remove(xy[0])
        xy.append(None)
        xy.append(None)

def delete_canvas(event):
    canvas.delete('all')
    xy[:] = [None,None,None,None,None,None]

canvas = tkinter.Canvas(width= "800", height= "700")
canvas.pack()

canvas.bind("<ButtonPress-1>", draw_polygon)
canvas.bind("<ButtonPress-3>", delete_canvas)

canvas.mainloop()