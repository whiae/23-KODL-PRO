ptaki = []

while(True):
    print("Jeżeli chcesz zakonczyć wpisz q")
    ptak = input("Nazwa nowego ptaka: ")
    if ptak != "q":
        ptaki.append(ptak)
    elif ptak == "q":
        print(ptaki)
        break;