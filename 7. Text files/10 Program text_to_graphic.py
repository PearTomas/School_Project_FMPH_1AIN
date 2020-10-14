'''
Vypíš obsah textového súboru do grafickej plochy. Súbor obsahuje niekoľko riadkov a funkcia vypis_subor(meno_suboru)
tieto riadky vypíše pod sebou nejakým fontom. V globálnej premennej canvas je referencia na grafickú plochu.

Writes the contents of a text file to the graphics area. The file contains several lines and the function file_list(file_path)
prints these lines below it in some font. In the global variable canvas, there is a reference to the graphics area.
'''

import tkinter
file_path = "text3.txt"
widht,height = "400","800"

canvas = tkinter.Canvas(width= widht, height= height)
canvas.pack()

x,y = int(widht)/2,20

with open(file_path, "r", encoding="utf-8")as t:
    for line in t:
        #canvas.create_text(x,y,text=line)

        #right alignment
        canvas.create_text(x-(x/2), y, text=line,anchor='nw')
        y += 20

tkinter.mainloop()