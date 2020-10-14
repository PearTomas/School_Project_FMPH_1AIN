'''
Napíš program, ktorý si vypýta meno súboru a potom vypíše všetky tie riadky súboru, ktoré obsahujú práve tri slová. V každom riadku je niekoľko slov, ktoré sú oddelené jednou medzerou.
Write a program that asks for the file name and then print all those lines that contain exactly three words. There are several words in each line, separated by one space.
'''

def GetFilePath(extension=".txt",ask="The name of the file?: "):
    path = input(ask)
    if path[-len(extension):] != extension:
        path += extension
    return path


with open(GetFilePath(),"r", encoding='utf-8') as t:
    text = t.readline()
    counter = 0
    while text:
        for i in text:
            if i == " ":
                counter +=1

        if counter == 2:
            print(text.rstrip())
        text = t.readline()
        counter = 0
