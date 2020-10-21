'''
Napíš funkciu z_dvojkovej(zoznam), ktorá dostane zoznam cifier dvojkového zápisu čísla v tvare z predchádzajúcej úlohy.
Funkcia vráti celé číslo (return), ktorého cifry v dvojkovej sústave zodpovedajú zadanému zoznamu.

Write a function from_double (list), which gets a list of binary digits of the number in the form from the previous task.
The function returns an integer (return), whose digits in the binary system correspond to the specified list.
'''

def binar2int(n):
    x = ""
    for i in n:
        x += str(i)
    return int(x,2)

print(binar2int([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))