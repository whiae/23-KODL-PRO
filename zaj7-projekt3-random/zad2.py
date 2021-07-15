import random

litery = "abcdefghijklmnoprstuwyzqxv"
cyfry = "0123456789"
haslo = ""
lbliter = 5
lbcyfr = 2

for j in range (7):
    if lbliter > 0:
        litera = random.choice(litery)
        haslo = haslo + litera
        lbliter = lbliter - 1
    if lbcyfr > 0:
        liczba = random.choice(cyfry)
        haslo = haslo + liczba
        lbcyfr = lbcyfr - 1

print("Wygenerowane hasło to:",haslo)