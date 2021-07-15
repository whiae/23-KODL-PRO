import random
import time

strzaly = 0
computer = random.randint(1,1000)
print("== START ==")
print("Komupter wylosował liczbę! Podaj swoją liczbę:")

while(True):
    user = int(input())
    if computer > user:
        print ("Podana liczba jest za mała, spróbuj jeszcze raz!\n")
        strzaly = strzaly + 1
    elif computer < user:
        print("Podana liczba jest za duża, spróbuj jeszcze raz!\n")
        strzaly = strzaly + 1
    elif computer == user:
        strzaly = strzaly + 1
        print("Brawo, udało Ci się odgadnąć liczbę!")
        print("Wylosowana przez komputer liczba to:",computer)
        print("Liczba oddanych strzałów:",strzaly)
        print("== KONIEC GRY ==")
        time.sleep(1)
        break;