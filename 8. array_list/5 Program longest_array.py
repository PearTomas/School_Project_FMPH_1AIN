'''
Napíš funkciu najdlhsie(zoznam), ktorá zo zoznamu slov vráti (return) najdlhšie slovo.
Funkcia nemodifikuje vstupný zoznam a nič nevypisuje.

Write the longest (list) function, which returns the longest word from the word list.
The function doesn't modify the input list and does not print anything.
'''

def longest_aray(list):
    length = 0
    for i in list:
        if len(i) > length:
            length = len(i)
            output = i
    return output

zoz = ['prvy', 'druhy', 'treti', 'stvrty', 'piaty']


print(longest_aray(zoz))