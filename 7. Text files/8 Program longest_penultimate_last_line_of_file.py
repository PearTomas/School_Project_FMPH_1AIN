'''
Napíš a otestuj tieto funkcie. Ich parametrom je meno nejakého textového súboru a všetky vrátia (return) nejaký jeden riadok súboru:
funkcia posledny_riadok(meno_suboru)
funkcia predposledny_riadok(meno_suboru)
funkcia najdlhsi_riadok(meno_suboru)

Write functions that return values:
function last_line (file name)
function penultimate_line (filename)
function longest_line (filename)
'''

def last_line(file_path):
    with open(file_path, "r", encoding="utf-8")as t:
        text = t.readline()
        lineX,lineY = "",""
        while text:
            lineX = text
            text = t.readline()
        return lineX.rstrip()

def penultimate_line(file_path):
    with open(file_path, "r", encoding="utf-8")as t:
        last = ""
        text = t.readline()
        enultimate = last
        last = text
        enultimate = last
        while text:
            text = t.readline()
            if text:
              enultimate = last
              last = text

        return enultimate.rstrip()

def longest_line(file_path):
    with open(file_path, "r", encoding="utf-8")as t:
        text = t.readline()
        long = 0
        longest = ""
        while text:
            if len(text) > long:
                long = len(text)
                longest = text
            text = t.readline()
        return longest.rstrip()






print(last_line("text3.txt"))
print(penultimate_line("text3.txt"))
print(longest_line("text3.txt"))