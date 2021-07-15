imiona = []
nazwiska = []
wyniki = []

print("== WYNIKI GRY ==\nDodaj nową osobę - a\nEdytuj osobe - e\nWyświetl listę - w\nZakończ - q")

while(True):
    znak = input()
    if znak == "a":
        print("Podaj imię:")
        imie = input()
        imiona.append(imie)
        print("Podaj nazwisko:")
        nazwisko = input()
        nazwiska.append(nazwisko)
        print("Podaj wynik:")
        wynik = input()
        wyniki.append(wynik)
        print("DODANO!\n")
    elif znak == "w":
        print("== LISTA WYNIKÓW ==")
        print(imiona)
        print(nazwiska)
        print(wyniki)
    elif znak == "q":
        print("KONIEC PROGRAMU!")
        break
    elif znak == "e":
        print("W której liście chcesz coś zmienić?")          
        zmiana = input()
        print("Na którym miejscu?")                           
        miejsce = int(input())
        if zmiana == "imiona":
            print("Proszę wpisać nową wartość:")
            imiona[miejsce] = input()
            print("ZMIENIONO!\n")
        elif zmiana == "nazwiska":
            print("Proszę wpisać nową wartość:")
            nazwiska[miejsce] = input()
            print("ZMIENIONO!\n")
        elif zmiana == "wyniki":
            print("Proszę wpisać nową wartość:")
            wyniki[miejsce] = input()
            print("ZMIENIONO!\n")
        else:
            print("Nie ma takiej tabeli!")
    else:
        print("Niepoprawny znak!")