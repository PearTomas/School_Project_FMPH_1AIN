'''
Napíš funkciu start(zoznam, n), ktorá z daného zoznamu znakových reťazcov vyrobí (a vráti) nový, v ktorom sa z každého
reťazca ponechá len prvých n znakov.

Write the function start (list, n), which produces (and returns) a new one from the given list of character strings,
in which only the first n characters are left from each string
'''
mesiace = ['januar', 'februar', 'marec', 'april', 'maj',
               'jun', 'jul', 'august', 'september',
               'oktober', 'november', 'december']

def star(list, n):
    output = []
    for i in list:
        output.append(i[:n])
        print(i)
    return output

mesiace_change = star(mesiace,3)
print(mesiace_change)
