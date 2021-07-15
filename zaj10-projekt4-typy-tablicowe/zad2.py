import random

lista = []

for i in range(0,30):
    liczba = random.randrange(0,99)
    lista.append(liczba)

print(lista)
print("Indeksy nieparzyste (indeksy rozpoczynają się od 0!):")
for i in range(len(lista)):
    if i % 2 != 0:
        print(lista[i])