'''
Program počas ťahania myši zabezpečí kreslenie žltých krúžkov, prvý s polomerom 1 každý ďalší je o 1 väčší.
Pravým klikom sa obrazovka zmaže a nastaví sa kreslenie od najmenšieho krúžku (s polomerom 1).

The program will draw yellow circles while dragging the mouse, the first with a radius of 1, each one is 1 larger.
Right-click to clear the screen and set the drawing from the smallest circle (with radius 1).
'''
import tkinter

r_global = [1]
def draw_circle(event):
    x,y = event.x , event.y
    r = int(r_global[0])
    canvas.create_oval(x+r,y+r,x-r,y-r,fill="yellow")
    r_global[0] =r_global[0] + 1 ;

def delete_canvas(event):
    canvas.delete('all')
    r_global[0] = 0

canvas = tkinter.Canvas(width= "1200", height= "700")
canvas.pack()

canvas.bind("<B1-Motion>", draw_circle)
canvas.bind("<ButtonPress-3>", delete_canvas)


canvas.mainloop()