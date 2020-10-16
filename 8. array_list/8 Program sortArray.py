'''
Napíš funkciu vzostupne(zoznam), ktorá zistí, či sú prvky vstupného zoznamu usporiadané vzostupne. Funkcia vráti (return)
True alebo False, nemodifikuje vstupný zoznam a nič nevypisuje. Nepoužívaj sort ani sorted.

Write a function ascending(list), which determines whether the elements of the input list are arranged in
ascending order. The function returns True or False, doesn't modify the input list, and does not print anything.
Do not use sort or sorted

napríklad / for example:
>>> ascending([100, 5, 5, 8, 100,])
True
>>> ascending(['pyton', 'python', 'pytliak'])
False
'''

def ascending(list):
    j = 0
    for i in range(1,len(list)):
        if list[i-1] <= list[i]:
            j += 1
    if j == len(list)-1:
        return True
    else:
        return False

x = [2, 5, 5, 8, 100,100,101]
y = ['pyton', 'python', 'pytliak']
print(ascending(x))
print(ascending(y))