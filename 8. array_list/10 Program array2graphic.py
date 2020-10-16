'''
Napíš funkciu kresli_text(zoznam), v ktorej parameter zoznam je troj alebo štvor prvkový zoznam.
Tento zoznam má na začiatku dve celé čísla (označujú súradnice x a y), tretím prvkom je znakový reťazec.
Štvrtým prvkom zoznamu je reťazec, ktorý špecifikuje font. Keď tento prvok chýba, použi 'arial 20'.
Funkcia vypíše do grafickej plochy na zadané súradnice daný reťazec s daným fontom.

Write a function draw_text(list) in which the list is a three or four element array.
This list initially has two integers (indicated by the x and y coordinates), the third element is a character string.
The fourth element of the list is a string that specifies the font. If this element is missing, use 'arial 20'.
The function writes the given string with the given font to the graphic area for the specified coordinates.
'''

def draw_text(list):
    x = int(list[0])
    y = int(list[1])
    text = str(list[2])
    if len(list) == 4:
        font = str(list[3])
    else:
        font = "arial 20"
    canvas.create_text(x,y,text=text,font=font)


import tkinter

canvas = tkinter.Canvas()
canvas.pack()

zoz = [200, 100, 'PYTHON']
draw_text(zoz)
draw_text([200, 150, 'programovanie', 'consolas 35'])
draw_text([200, 60, 'najlepšie je', 'tahoma 15'])
tkinter.mainloop()