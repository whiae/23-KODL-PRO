import time

print("== START ==\nPodaj liczbę sekund:")
sekundy = int(input())

while sekundy > 0:
    time.sleep(1)
    sekundy = sekundy - 1
    print(sekundy)
print("DRRRRRR!")