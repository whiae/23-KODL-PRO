slownik = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X",50:"L",100:"C",500:"D",1000:"M"}

print("Jakią liczbę chcesz zamienić?")
liczba = int(input())
if liczba in slownik:
    print(slownik.get(liczba))
else:
    print("Nie znam takiej liczby")