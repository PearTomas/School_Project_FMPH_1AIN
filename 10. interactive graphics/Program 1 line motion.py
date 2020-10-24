'''
Napíš program, ktorý zabezpečí ťahanie myši: pri ťahaní sa kreslia vodorovné úsečky (z kliknutej pozície dĺžky 100).
Pravým klikom sa obrazovka zmaže.

Write a program that will ensure mouse dragging: when dragging, horizontal lines are drawn
(from a clicked position of length 100). Right-click to clear the screen.
'''

import tkinter

def draw_line(event):
    x, y = event.x, event.y
    canvas.create_line(x-50,y,x+50,y)

def delete_canvas(event):
    canvas.delete('all')

canvas = tkinter.Canvas()
canvas.pack()

canvas.bind("<B1-Motion>", draw_line)
canvas.bind("<ButtonPress-3>", delete_canvas)


canvas.mainloop()