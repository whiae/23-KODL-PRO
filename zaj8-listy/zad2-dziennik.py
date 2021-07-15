przedmioty = ["język polski", "język angielski", "matematyka", "fizyka", "chemia", "biologia"]
oceny = []
suma = 0

for i in range(len(przedmioty)):
    print("Wpisz otrzymaną ocenę z przedmiotu",przedmioty[i])
    oceny.append(int(input()))

for i in range(len(przedmioty)):
        print("Ocena z przedmiotu",przedmioty[i], "to:", oceny[i])

##for i in oceny:
##    suma = suma + i

for i in range(len(oceny)):
    suma = suma + oceny[i]

srednia = suma / len(oceny)
print("Średia ocen:",srednia)