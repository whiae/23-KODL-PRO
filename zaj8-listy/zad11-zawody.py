imiona = ["Asia","Basia","Kasia","Arek","Jarek"]
zawody = ["lekarz","piekarz","kucharz","piekarz","lekarz"]

print("Jaki zawód wyświetlić?")
kto = input()

for i in range(len(zawody)):
    if zawody[i] == kto:
        print(imiona[i])