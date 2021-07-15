wynik = 0
for i in range(25,51):
    if i % 2 == 0:
        #print(str(i))
        wynik = wynik+i
    else:
        continue
print("Wynik to: " + str(wynik) + "\n")

wynik2 = 0
j = 25
while j >= 25 and j <= 50:
    if j % 2 == 0:
        #print(str(j))
        wynik2 = wynik2+j
        j = j+1
    else:
        j = j+1
        continue

print("Wynik to: " + str(wynik2))
