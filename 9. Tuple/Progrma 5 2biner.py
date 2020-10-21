'''
Napíš funkciu dvojkova(cislo), ktorá vráti (return) zoznam cifier daného čísla v dvojkovej sústave. Využi f'{cislo:b}'

Write a binary function (number), which returns (return) a list of digits of the given number in the binary system.
Use f '{number: b}'
'''


def binar(n):
    binar2 = f'{n:b}'
    result = [0]*len(binar2)
    for i,j in enumerate(binar2):
        result[i] = int(j)
    return result

print(binar(11213))