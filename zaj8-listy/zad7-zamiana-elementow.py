lista = []

for i in range(0,51):
    lista.append(0)

for j in range(len(lista)):
    if j %2 == 0:
        lista[j] = 2
    elif j %3 == 0:
        lista[j] = 3
    elif j %5 == 0:
        lista[j] = 5

for k in lista[:]:
    if k == 0:
        lista.remove(k)

lista.sort()
print(lista)