'''
Napíš funkciu ity(meno_suboru, index), ktorá z daného súboru vráti (return) riadok s daným poradovým číslom (index). Riadky číslujeme od 0.
Write the function ity(file:path, index), which returns a line with the given sequence number (index) from the given file. We number the lines from 0.
'''

def ity(file_path, index):
    with open(file_path, "r", encoding="utf-8")as t:
        for i in range(index):
            text = t.readline()
        return text

print(ity("text3.txt", 5))