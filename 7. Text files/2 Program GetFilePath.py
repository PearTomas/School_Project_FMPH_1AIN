'''
Napíš program, ktorý si vypýta meno súboru a potom vypíše každý druhý znak z prvého riadka tohto súboru.
Write a program that asks for a file name and then prints every other character from the first line of that file.
'''


def GetFilePath(extension=".txt", ask="The name of the file?: "):
    path = input(ask)
    if path[-len(extension):] != extension:
        path += extension
    return path


with open(GetFilePath(), "r", encoding='utf-8') as t:
    first_line = t.readline()
print(first_line[1:-1:2])
