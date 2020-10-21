'''
Napíš funkciu dve_kocky(pocet), ktorá vráti 13-prvkový zoznam celých čísel. Tento sa skonštruuje takto:
zadaný pocet-krát hodí dvoma kockami (dve nádodné čísla od 1 do 6), pre každý takýto hod urobí ich súčet
a v 13-prvkovom zozname si eviduje počet výskytov každého súčtu, napríklad zoznam[5] bude označovať, koľko
krát pri našej simulácii padol súčet 5; zrejme na začiatku budú v zozname samé 0 a potom pri každom hode sa
číslo na príslušnom indexe zvýši o 1. Funkcia nič nevypisuje, len vráti vytvorený 13-prvkový zoznam celých čísel.

Write a function two_cubes (number), which returns a 13-element list of integers. This is constructed as follows:
entered number of times rolls two dice (two race numbers from 1 to 6), for each such roll makes their sum
and in the 13-element list it records the number of occurrences of each sum, for example the list [5] will indicate how
many times in our simulation the sum fell 5; apparently at the beginning there will be only 0 in the list and then with
each roll increments the number on the relevant index by 1. The function does not print anything, it only returns the
created 13-element list of integers.
'''
from random import randint

def two_dice(n):

    result = [0]*13
    for i in range(n):
        x = randint(1,6) + randint(1,6)
        result[x] += 1
    return result

two_dice(1000)
#Test
#print(two_dice(1000))
