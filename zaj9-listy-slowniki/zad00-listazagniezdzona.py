import random
lista = []
for i in range(3):
    sublista = []
    for j in range(5):
        sublista.append(random.randint(0, 9))
    lista.append(sublista)
print(lista)