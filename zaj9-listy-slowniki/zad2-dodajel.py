lista = [1,2,3,4,5,6,7,8,9,10]

suma = 0
for i in lista:
    suma = suma + i
print("Suma liczb:",suma)

print("Podaj liczbę:")
liczba = input()
lista.append(liczba)
print("Lista z nowym elementem:",lista)