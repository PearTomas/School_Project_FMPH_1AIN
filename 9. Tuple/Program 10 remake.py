'''
Napíš funkciu prerob(cislo), ktorá z daného celého čísla vyrobí reťazec, ale tak, že cifry zoskupí do trojíc (sprava)
a oddelí podčiarkovníkom. Využi funkciu join, preto z čísla najprv vyrob zoznam trojznakových reťazcov.
Funkcia nič nevypisuje, ale vráti (return) výsledný reťazec.

Write a rework function (number), which produces a string from a given integer, but by grouping the digits into triplets (right)
and separate the underscores. It will use the join function, so first make a list of three-character strings from the number.
The function does not print anything, but returns the resulting string.
'''

def remake(n):
    n = str(n)
    x = [0]*(1 + len(n)//3)
    x[0] = n[:(len(n)) % 3]
    n = n[((len(n)) % 3)-1:]
    for i,j in enumerate(range(0,len(n)-1,3)):
        x[i+1] = n[j+1:j+4]
    return "_".join(x)


print(remake(12345678))