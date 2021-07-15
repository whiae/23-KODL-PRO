import random

lista = []
liczba = 0
suma = 0


for i in range(0,10):
    liczba = random.randrange(0,100)
    lista.append(liczba)
    suma = suma + liczba

srednia = suma / 10
print(lista)
print("Element minimalny to:", min(lista))
print("Element maksymalny to:", max(lista))
print("Średnia wartość elementów:", srednia)

""" MINIMUM I MAKSIMUM:
    SORT / SORT REVERSE
    LISTA.POP 
    
    LUB 
    
    if liczba > max:
        max = liczba
    elif liczba < min:
        min = liczba
"""