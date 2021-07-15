import random

print("Podaj n:")
n = int(input())
print("Podaj m:")
m = int(input())
tablica = []

for i in range(n):
    sublista = []
    for j in range(m):
        sublista.append(random.randint(0, 99))
    tablica.append(sublista)
print(tablica)