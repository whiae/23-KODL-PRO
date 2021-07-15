import random
import time

print("== START ==\nWybierz:")
wybor = input()
mozliwosci = ["kamien", "papier", "nozyce", "jaszczurka", "spock"]
print("Losuję...")
time.sleep(1)
komputer = random.choice(mozliwosci)
print("Komputer wybrał:", komputer, "\n")

if wybor == "kamien" and (komputer == "papier" or komputer == "spock"):
    print("Wygrał komputer!")
elif wybor == "kamien" and (komputer == "nozyce" or komputer == "jaszczurka"):
    print("Wygrałeś!")

if wybor == "papier" and (komputer == "nozyce" or komputer == "jaszczurka"):
    print("Wygrał komputer!")
elif wybor == "papier" and (komputer == "kamien" or komputer == "spock"):
    print("Wygrałeś!")

if wybor == "nozyce" and (komputer == "kamien" or komputer == "spock"):
    print("Wygrał komputer!")
elif wybor == "nozyce" and (komputer == "papier" or komputer == "jaszurka"):
    print("Wygrałeś!")

if wybor == "jaszczurka" and (komputer == "nozyczki" or komputer == "kamien"):
    print("Wygrał komputer!")
elif wybor == "jaszczurka" and (komputer == "spock" or komputer == "papier"):
    print("Wygrałeś!")

if wybor == "spock" and (komputer == "papier" or komputer == "jaszczurka"):
    print("Wygrał komputer!")
elif wybor == "spock" and (komputer == "kamien" or komputer == "nozyczki"):
    print("Wygrałeś!")

elif wybor == komputer:
    print("Remis!")
