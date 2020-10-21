'''
Ak by si postupnosť 100 náhodných bodov z predchádzajúcej úlohy vykreslil pomocou create_line, dostal by si nejakú
čmáranicu (vyskúšaj). Ďalej otestuj, ako sa vykreslí táto postupnosť, keď sa najprv usporiada pomocou funkcie sorted

If you plotted a sequence of 100 random points from a previous task using create_line, you would get some
doodle. Next, test how this sequence is rendered when it is first organized using the "sorted" function
'''
import tkinter
from random import randint

def random_x_y(n):
    result = [0]*(n)
    for i in range(n):
        result[i] = (randint(0,380),randint(0,260))
    print(result)
    return result

def line_draw(n):
    x_y = sorted(random_x_y(n))
    for i in range(n-1):
        xy = x_y[0+i]
        xy1 = x_y[1+i]
        canvas.create_line(xy,xy1)



canvas = tkinter.Canvas()
canvas.pack()

line_draw(100)

tkinter.mainloop()