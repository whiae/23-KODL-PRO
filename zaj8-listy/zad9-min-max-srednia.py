import random

lista = []
min = 99
max = 0
suma = 0

for i in range(0,21):
    liczba = random.randint(0,99)
    lista.append(liczba)
    suma = suma + liczba
    if liczba > max:
        max = liczba
    elif liczba < min:
        min = liczba

print(lista)
srednia = suma / len(lista)
print("== PODSUMOWANIE ==")
print("Minimum:",min,"Maksimum:",max)
print("Średnia:",srednia)