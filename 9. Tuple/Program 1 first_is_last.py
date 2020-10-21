'''
Napíš funkciu posun(zoznam), ktorá posunie prvky v danom zozname tak, že prvý sa presťahuje na koniec.
Funkcia nič nevracia, len zmení obsah pôvodného zoznamu

Write a move(list) function that moves the elements in the list so that the first one moves to the end.
The function returns nothing, just changes the contents of the original list
'''

def move(list):
    list.append(list[0])
    list.remove(list[0])


a = [2, 3, '5', 7, 11]
a = 'kto druhemu jamu kope'.split()

for i in range(5):
        print(a)
        move(a)