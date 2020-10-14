'''
Napíš funkciu vyrob(meno_suboru, pocet, text), ktorá vytvorí textový súbor s daným menom. Tento súbor bude pythonovským
skriptom, ktorý príslušný pocet krát vypíše (pomocou print()) zadaný text. Tento skript by mal na opakovanie výpisu
využiť while-cyklus (nie for-cyklus)

Write a function make(filename, count, text) that creates a text file with the given name.
This file will be a Python script that prints the specified number of times (using print()).
This script should use a while-loop (not a for-loop) to repeat the statement.
'''

def make(file_name, count=1, text=""):
    with open(file_name, "w", encoding="utf-8")as f:
        f.write(f"i = 0\nwhile i < {count}:\n\tprint(\"{text}\")\n\ti +=1")


make("ahoj.py",5,"ahoj.sk")