'''
Napíš funkciu nahodne_body(pocet), ktorá vráti zadaný počet náhodných bodov v grafickej ploche (dvojíc čísel z 380x260).
Funkcia vráti zoznam, ktorý bude obsahovať dvojprvkové n-tice celých čísel.

Write a function random_points (number), which returns the specified number of random points in the graphics area
(pairs of numbers from 380x260).
The function returns a list that contains two-element n-tuples of integers.

'''
from random import randint

def random_x_y(n):
    result = [0]*(n+1)
    for i in range(n):
        result[i] = (randint(0,380),randint(0,260))
    return result

print(random_x_y(5))
