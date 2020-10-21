'''
Napíš funkciu desiatkova(cislo), ktorá vráti (return) zoznam cifier daného čísla v desiatkovej sústave.
Využi funkcie str a int

Write a decimal (number) function that returns a list of digits of a given number in the decimal system.
It will use the functions str and int
'''

def decimal_sys(number):
    result = [0]*(len(str(number)))
    number = str(number)
    for i,j in enumerate(number):
        result[i] = int(j)
    return result

decimal_sys(11213)
#Test
#print(decimal_sys(11213))
#print(sum(decimal_sys(11213)))