'''
Do premenných den a day priraď 7 názvov dní v týždni v slovenčine a v angličtine ('pondelok', … ):
make arraylist contain 7 day of the week in Slovak language and another array for English days

Vypíš tieto dva zoznamy každý do jedného riadku (slová v riadku oddeľ medzerami)
Write these two lists each in one line (words in the line separated by spaces)

Vypíš tieto dva zoznamy každý do jedného riadku (slová v riadku oddeľ medzerami)
Write these two lists each in one line (words in the line separated by spaces)
'''

den = ["pondelok","utorok","streda","štvrtok","piatok","sobota","nedela"]
day = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

output = ""
for i in den:
    print(i, end=" ")
print()
for i in day:
    print(i, end=" ")
print(end="\n\n")

for x in range(len(den)):
    print(den[x], day[x])
