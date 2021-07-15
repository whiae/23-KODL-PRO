lista = []

print("Ile liczb pobrać?")
dlugosc = int(input())

for i in range(dlugosc):
    print("Wpisz liczbę:")
    lista.append(int(input()))

print(lista)

"""for i in lista:
    if i % 2 == 0:
        print(i, "parzysta")
    else:
        print(i, "nieparzysta")
"""

for i in range(len(lista)):
    if i % 2 == 0:
        print(lista[i], "parzysta")
    else:
        print(lista[i], "nieparzysta")