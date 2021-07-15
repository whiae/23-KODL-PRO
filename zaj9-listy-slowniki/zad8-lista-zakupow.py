ceny = {"chleb": 4.5, "pomidory": 6, "masło": 9.99, "herbata": 5.75, "ser": 4.99}

suma = 0
print("Co chcesz dodać do listy zakupów?\nAby zakończyć i wyświetlić sumę - 1")

while(True):
    produkt = input()
    if produkt in ceny:
        suma = suma + ceny.get(produkt)
        print("Dodano!")
    elif produkt == "1":
        print("Suma:",suma)
        break
    else:
        print("Nie ma takiego produktu!")
