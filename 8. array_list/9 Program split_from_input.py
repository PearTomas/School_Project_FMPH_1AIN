'''
Napíš funkciu rozdel(retazec), ktorá daný reťazec rozdelí na podreťazce a tieto vráti ako zoznam reťazcov.
Podreťazce sú navzájom oddelené aspoň jednou medzerou alebo znakom '\n'. Funkcia nič nevypisuje. Nepoužívaj split

Write a split(string) function that splits the string into substrings and returns them as a list of strings.
Substrings are separated from each other by at least one space or '\ n' character. The function does not print anything.
Don't use .split
'''

def split_input(string):
    output = []
    verb = ""
    for i,string in enumerate(string):
        if string == "\n":
            output.append(verb)
            verb = ""
        else:
            verb += string
    return output

print(split_input("ahoj\nako\nsa\nmas\n?\n\n"))
