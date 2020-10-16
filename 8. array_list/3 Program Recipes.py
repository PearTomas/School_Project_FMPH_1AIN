'''
Napíš funkciu vypis_recept(zoznam), ktorá takýto zoznam vypíše (pomocou print) do viacerých riadkov po troch

Write the function get_recipe(list), which prints such a list (using print) in several lines of three
'''
recipe = ['cukor', 100, 'g', 'vajíčka', 5, 'ks', 'mlieko', 2, 'dcl', "soľ",2,"štipky"]

def get_recipe(list,s=""):
    for i in range(3,int(len(list)+3),3):
        print(((((str(recipe[i-3:i])).replace("\'","")).replace("[","")).replace("]","")).replace(",",""))
        #print(str(recipe[i-3:i]))

get_recipe(recipe)