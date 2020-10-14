'''
Napíš funkciu nahodne_cisla(meno_suboru, pocet). Funkcia vytvorí textový súbor s trojcifernými náhodnými číslami .
V každom riadku bude jedno číslo, riadkov bude zadaný počet.

Write the function random_numbers (file_path_and_name, count). The function creates a text file with three-digit random numbers.
There will be one number in each line, the number of lines will be specified.
'''
from random import randint

def random_number(file_path_and_name, count):
    with open(file_path_and_name, "w", encoding="utf-8")as f:
        for i in range(count):
            #f.write(str(randint(100,999))+"\n")
            print(randint(100,999), file=f)
    return f"Done, file {file_path_and_name} was created and fill with {count} random three-digit numbers "

print(random_number("test1.txt",20))