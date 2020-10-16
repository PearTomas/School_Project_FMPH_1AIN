'''
V nejakej obci je jediná ulica, na ktorej je n domov. Na miestnom úrade majú v zozname (typu list) pre každý dom
zaznačený počet obyvateľov. Pomocou len štyroch print vypíš, koľko obyvateľov žije v celej obci, koľko domov je
neobývaných, aký je maximálny počet obyvateľov v dome a v koľkých domoch býva tento maximálny počet.

In a village there is only one street on which there is a home. At the local authority, they have a number of
inhabitants marked in the list (letter type) for each house. Use only four prints to write how many inhabitants
live in the whole village, how many houses are uninhabited, what is the maximum number of inhabitants in the
house and how many houses this maximum number lives in.
'''

houses = [4, 2, 0, 5, 0, 1, 5, 4]
print("the population is",sum(houses))
print("unoccupied houses:",houses.count(0))
print("the maximum number of inhabitants in the house is:",max(houses))
print("number of maximum houses",houses.count(max(houses)))
