import random
lista1 = []
lista2 = []

for i in range(11):
    lista1.append(random.randint(0,100))

for j in reversed(lista1):
    lista2.append(j)

print(lista1)
print(lista2)

## REVERSE