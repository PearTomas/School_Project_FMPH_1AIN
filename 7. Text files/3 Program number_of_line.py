'''
Napíš program, ktorý si vypýta meno súboru a potom vypíše počet riadkov a dĺžku najdlhšieho riadka (aj s koncovým '\n')
Write a program that asks for the file name and then prints the number of lines and the length of the longest line (even with the ending '\ n')
'''

path = input(f"The name of the file?: ")
if path[-len(".txt"):] != ".txt":
    path += ".txt"

with open(path, "r", encoding="utf-8")as t:
    text = t.readline()
    length, longest, number_of_line = 0, 0, 0,
    while text:
        length = len(text)

        if length > longest:
            longest = length
        text = t.readline()
        number_of_line += 1

print("File name:", path)
print("Number of file lines:", number_of_line)
print(f"The longest line is {longest} characters")
