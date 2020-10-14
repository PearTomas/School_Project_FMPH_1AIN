'''
Napíš program, ktorý si vypýta meno súboru a z tohto súboru vypíše druhý riadok.
Write a program that asks for the name of the file and prints the second line from the file.
'''


def which_line(riadok, file_path):
    file = open(file_path, "r", encoding='utf-8')
    for i in range(riadok - 1):
        file.readline()
    x = file.readline()
    return x.rstrip()


path = input("the name of the file?: ")
if path[-4:] != ".txt":
    path += ".txt"

print(which_line(2, path))
