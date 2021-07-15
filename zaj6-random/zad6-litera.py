import random
import time

print("Aby rozpocząć wciśnij s!")
zakres = "abcdefghijklmnoprstuwyzqxv"

while(True):
    znak1 = input()
    if znak1 == "s":
        print("Losuję literę!")
        wylosowana = random.choice(zakres)
        print("Wylosowana litera to:", wylosowana)
        start = time.time()
        znak2 = 0
        while znak2 != wylosowana:
            print("Nie wcisnąłeś", wylosowana)
            znak2 = input()
        koniec = time.time()
        czas_trwania = koniec - start
        print("Na wciśnięcie potrzebowałeś:", czas_trwania)