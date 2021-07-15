import random

lista = []

for i in range(31):
    liczba = random.uniform(3.0,4.0)
    zaokraglona = round(liczba, 4)
    lista.append(zaokraglona)

print(lista)