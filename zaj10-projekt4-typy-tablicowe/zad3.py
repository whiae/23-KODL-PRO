lista = []
ilerazy = 0

print("Podaj długość listy: ")
n = int(input())

for i in range (n):
    print("Podaj liczbę: ")
    liczba = int(input())
    lista.append(liczba)

print("Twoja lista:",lista)

lista.sort()
min = lista[0]

for j in lista:
    if j == min:
        ilerazy = ilerazy + 1

print("Najmniejszy element listy to:",min)
print("Wystąpił on:",ilerazy,"razy")
