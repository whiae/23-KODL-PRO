import operator

imiona = ["Asia","Kasia","Basia","Arek","Jarek"]
zarobki = [3000,3500,2500,5000,3000]
lista = imiona, zarobki

print("== WYNIKI GRY ==\nDodaj nową osobę - a\nWyświetl listę - w\nZakończ program - q\n")

while (True):
    znak = input()
    if znak == "a":
        print("Podaj imię:")
        imie = input()
        imiona.append(imie)
        print("Podaj zarobki:")
        money = input()
        zarobki.append(money)
        print("DODANO!\n")
    elif znak == "w":
        print(lista)
        print("== POSORTOWANA LISTA ==")
        lista.sort(key=operator.itemgetter(1))
        print(lista)
    elif znak == "q":
        print("KONIEC PROGRAMU!")
        break
    else:
        print("Nieprawidłowy znak!\n")