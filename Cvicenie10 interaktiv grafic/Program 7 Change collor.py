'''
Najprv zadefinuj štyri premenné (napríklad x1, y1, x2, y2 = 100, 50, 200, 100) a pomocou nich nakresli farebný obdĺžnik.
ňPotom program pri každom kliknutí, ale len do vnútra obdĺžnika, mu zmení farbu výplne. Každé kliknutie do vnútra
obdĺžnika cyklicky strieda jednu zo 4 farieb, napríklad farby = ['blue', 'red', 'green', 'yellow'].

First, define four variables (for example, x1, y1, x2, y2 = 100, 50, 200, 100) and use them to draw a colored rectangle.
ňThen the program, with each click, but only inside the rectangle, it changes the color of the fill. Every click inside
the rectangle cyclically alternates one of 4 colors, for example colors = ['blue', 'red', 'green', 'yellow'].
'''
import tkinter

#Funkcia z Cvicenia9 Program1 first_is_last \\ Function from Exercise 9 "Program1 first_is_last"
def move(list):
    list.append(list[0])
    list.remove(list[0])

rec = [100, 50, 200, 100]
color = ['blue', 'red', 'green', 'yellow']
def change_color(pos):
    if rec[0] <= pos.x <= rec[2] and rec[1] <= pos.y <= rec[3]:
        move(color)
        canvas.delete("myRec")
        canvas.create_rectangle(rec,fill=color[0],tag="myRec")


canvas = tkinter.Canvas(width= "300", height= "150")
canvas.pack()
canvas.create_rectangle(rec,fill=color[0],tag = "myRec")
canvas.bind("<ButtonPress-1>", change_color)


canvas.mainloop()