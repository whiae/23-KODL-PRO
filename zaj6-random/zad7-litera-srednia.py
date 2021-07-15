import random
import time

print("== START ==")
zakres = "abcdefghijklmnoprstuwyzqxv"
i = 0
suma = 0

while i < 5:
    print("Losuję literę!")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    wylosowana = random.choice(zakres)
    print("Wylosowana litera to:", wylosowana)
    start = time.time()
    znak = input()
    while znak != wylosowana:
        print("Nie wcisnąłeś", wylosowana)
        znak = input()
    koniec = time.time()
    czas_trwania = koniec - start
    suma = suma + czas_trwania
    print("Na wciśnięcie potrzebowałeś:", czas_trwania)
    i = i+1

sredni = suma / 5
print("Średni czas:", sredni)