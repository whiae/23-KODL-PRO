import random

print("== START ==\nPodaj liczbe:")
liczba = int(input())

komputer = random.randint(0,100)
print("Liczba wylosowana przez komputer to:", komputer)

if liczba > komputer:
    print("Wygrałeś!")
elif liczba == komputer:
    print("Remis!")
elif liczba < komputer:
    print("Wygrał komputer!")