import random

print("+---+------+")
for i in range(7):
    liczba = random.random()
    zaokraglona = round(liczba, 2)
    print("|",i,"|",zaokraglona,"|")
print("+---+------+")