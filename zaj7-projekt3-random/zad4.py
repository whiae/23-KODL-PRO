import random
import time

print("== START ==")
print("Aby wyświetlić informacje o autorze - i")
print("Pierwsze zadanie - a")
print("Drugie zadanie - b")
print("Trzecie zadanie - c")
print("Aby zakończyć działanie programu - q\n")
print("Twój wybór:")

while(True):
    znak = input()
    if znak == "i":
        print("Weronika Szczegodzińska")
        print("Kognitywistyka, I rok, semestr 2.\n")
    elif znak == "a":
        print("Zadanie pierwsze:")
        suma = 10

        for i in range(10):
            suma = suma + random.randint(-10, 10)
        print("Twój stan portfela po 10 dniach to:", suma,"\n")
    elif znak == "b":
        print("Zadanie 2:")
        litery = "abcdefghijklmnoprstuwyzqxv"
        cyfry = "0123456789"
        haslo = ""
        lbliter = 5
        lbcyfr = 2

        for j in range(7):
            if lbliter > 0:
                litera = random.choice(litery)
                haslo = haslo + litera
                lbliter = lbliter - 1
            if lbcyfr > 0:
                liczba = random.choice(cyfry)
                haslo = haslo + liczba
                lbcyfr = lbcyfr - 1

        print("Wygenerowane hasło to:", haslo,"\n")
    elif znak == "c":
        print("Zadanie 3:")
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
    elif znak == "q":
        print("== KONIEC PROGRAMU ==")
        time.sleep(1)
        break;
    else:
        print("Wprowadzono nieprawidłowy znak!")