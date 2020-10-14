'''
Napíš funkciu riadky_s_textom(meno_suboru, text), ktorá otvorí zadaný súbor (môže byť aj súbor s pythonovským programom) a vypíše z neho len tie riadky, ktoré obsahujú zadaný text.
Write the function lines_with_text (file_name, text), which opens the file (it can also be a file with a Python program) and lists only those lines that contain the specified text.
'''

def lines_with_text(file_path, find_text):
    with open(file_path, "r", encoding="utf-8")as t:
        text = t.readline()
        output = ""
        while text:
            found = text.find(find_text)
            if found != -1:
                output += text
            text = t.readline()
    return output

print(lines_with_text("text3.txt", "ľ"))