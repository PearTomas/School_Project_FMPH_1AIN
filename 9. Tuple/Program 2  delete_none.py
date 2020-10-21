'''
Napíš funkciu vyhod_none(ntica), ktorá z danej n-tice vyhodí všetky výskyty None.
Funkcia vráti (return) túto novú n-ticu (nič nevypisuje).

Write the function hodhod_none (ntica), which discards all occurrences of None from the given n-tuple.
The function returns this new n-tuple.
'''

def delete_none(tuplex):
    tuplex = list(tuplex)
    while None in tuplex:
        tuplex.remove(None)
    tuplex = tuple(tuplex)
    return tuplex

delete_none((None,1,None,None))

#Test
'''
test = None,1,None,"AHOJ",None
print(test)
print(delete_none(test))
'''