'''
Napíš funkciu cele(zoznam), ktorá z daného zoznamu vytvorí (a vráti) nový, v ktorom sa každý prvok previedol
(pomocou funkcie int()) na celočíselnú hodnotu. Funkcia nemodifikuje vstupný zoznam a nič nevypisuje.

Write a function cell(list) that creates (and returns) a new one from that list, in which each element has been converted
(using the int () function) to an integer value. The function does not modify the input list and does not print anything.
'''

def s2i(list):
    output = []
    for i in list:
        output.append(int(i))
    return output

x = s2i(list(str(2**20)))
print(x)