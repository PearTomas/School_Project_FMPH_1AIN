'''
Napíš funkciu sort_y(zoznam), kde zoznam obsahuje dvojice (typ tuple) celých čísel. Tieto reprezentujú súradnice (x, y)
nejakých bodov v rovine. Tento zoznam treba usporiadať od najmenšieho po najväčší, lenže podľa druhých prvkov dvojíc
(y-ových súradníc). Uvedom si, že volanie zoznam.sort() by usporiadalo zoznam podľa prvých prvkov dvojíc (x-ových súradníc).

Write a function sort_y (list), where the list contains pairs (tuple type) of integers. These represent the coordinates
(x, y) some points in the plane. This list must be arranged from the smallest to the largest, but according to the
second elements of the pairs (y-coordinates). Note that calling seznam.sort () would arrange the list according to the
first elements of the pairs (x-coordinates).

'''

def sort_y(zoznam):
    for i, (x, y) in enumerate(zoznam):
        #print(x,y)
        zoznam[i] = (y, x)
    zoznam.sort()
    for i, (y, x) in enumerate(zoznam):
        zoznam[i] = (x, y)
    return zoznam



xy = [(100, 30), (200, 10), (300, 20)]
print(sort_y(xy))