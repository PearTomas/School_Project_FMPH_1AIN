'''
Napíš funkciu histogram(zoznam), ktorá z daného zoznamu čísel nakreslí stĺpcový diagram (obdĺžniky rovnakej šírky
a výšky podľa číselnej hodnoty zo zoznamu). Obdĺžniky budú mať takú šírku, aby čo najlepšie vyplnili šírku plochy 360
a budú mať náhodne zafarbenú výplň. Funkcia nemodifikuje vstupný zoznam. Môžeš počítať s tým, že všetky hodnoty
v zozname nie sú väčšie ako 240

Write a histogram (list) function that draws a bar chart (rectangles of the same width from a given list of numbers)
and height by numerical value from the list). The rectangles will be wide enough to fill the width of the area 360 as best as possible
and will have a randomly colored fill. The function does not modify the input list. You can count on all values
in the list are not greater than 240
'''

def histogram(list):
    star = 450
    offset = 5
    x = (int(width)-10)//len(list)
    for i,l in enumerate(list):
        y = int(l)
        color = (f'#{randrange(256 ** 3):06x}')
        canvas.create_rectangle(x*i+offset,star-y,x*i+x+offset,star,fill = color)


import tkinter
from random import randrange

width = "360"
canvas = tkinter.Canvas(height = "500",width = width )
canvas.pack()

histogram([120, 220, 180, 80, 90, 30, 200, 190, 240, 150])

tkinter.mainloop()