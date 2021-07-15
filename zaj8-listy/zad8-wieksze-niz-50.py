import random

lista = []

for i in range(0,21):
    lista.append(random.randint(0,99))

print(lista)

for i in lista[:]:
    if i > 50:
        lista.remove(i)

print(lista)