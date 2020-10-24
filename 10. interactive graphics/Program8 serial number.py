'''
Napíš program, ktorý pri každom kliknutí do grafickej plochy vypíše na toto miesto poradové číslo kliknutia,
teda postupne čísla 1, 2, 3, 4, … Nepoužívaj global (môžeš využiť globálnu premennú s nejakým zoznamom).

Write a program that, each time you click in the graphics area, print the serial number of the click in this place,
so sequentially the numbers 1, 2, 3, 4,… Don't use global (you can use a global variable with some list).
'''
import tkinter

turn = [1]

def serial_number(event):
    canvas.create_text(event.x,event.y,text=turn[0])
    turn[0] += 1

canvas = tkinter.Canvas(width= "1200", height= "700")
canvas.pack()
canvas.bind("<ButtonPress-1>", serial_number)

canvas.mainloop()