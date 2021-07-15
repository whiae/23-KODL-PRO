import random
lista = []
ilosc = 0

for i in range(101):
    lista.append(random.randint(0,100))

for j in lista:
    if j == 7:
        ilosc = ilosc + 1

#for j in range(len(lista)):
#    if lista[j] == 7:
#        ilosc = ilosc + 1

print(lista)
print("Ilość wylosowanych siódemek:",ilosc)

## LISTA.COUNT(7)
