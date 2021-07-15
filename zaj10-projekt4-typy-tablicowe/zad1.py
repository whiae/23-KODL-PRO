import random

lista = []

for i in range(0,30):
    liczba = random.randrange(0,99)
    lista.append(liczba)

##print(lista)
print("Wartości większe niż 60:")
for i in lista:
    if i > 60:
        print(i)