'''
Napíš funkciu vypis(zoznam, pocet), ktorá prvky daného zoznamu vypíše tak, že v každom riadku vypíše presne zadaný pocet
prvkov zoznamu.

Write a function line_spacing(list, number), which lists the elements of the given list by listing the exact specified
number of list elements in each line.
'''

def line_spacing(list,array_per_line):
    output = ""
    length = len(list)

    for j in range(0,length - length%array_per_line,array_per_line):
        for i in range(j,j+array_per_line):
            output += str(list[i]) + " "
        print(output)
        output = ""
    for i in range(length % array_per_line):
        output += str(list[length - length%array_per_line+i]) + " "
    print(output)

abzx = list(range(0,24))
print(abzx)
line_spacing(abzx,5)