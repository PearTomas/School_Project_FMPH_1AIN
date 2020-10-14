'''
Napíš funkciu priemer(meno_suboru), ktorá otvorí a číta zadaný súbor. V každom riadku tohto súboru je jedno celé číslo. Funkcia zistí priemer týchto hodnôt.
Write a function to average(filename) that opens and reads the specified file. There is one integer in each line of this file. The function calculates the average of these values.
'''
def average(file_path):
    with open(file_path, "r", encoding="utf-8")as t:
        text = t.readline()
        sum_up = 0
        count = 0
        while text:
            sum_up += int(text.rstrip())
            count += 1
            text = t.readline()
        return round(sum_up/count,2)


print(average("numbers.txt"))