print("Podaj liczbe:")
liczba = int(input())

if liczba % 2 == 0:
    print("liczba parzysta")
    wynik = liczba / 2
    print("wynik podzielenia przez 2: " + str(wynik))
else:
    print("liczba nieparzysta")
    if (liczba > 10):
        print("liczba jest duza")
    elif (liczba <= 10):
        print("liczba jest mala")