ksiazka = {"Ania Kowalska":600300400, "Basia Nowak":660300245}

print("Aby wyświetlić książkę - w\nAby dodać numer - a\nAby usunąć numer - r\nAby zmodyfikować istniejący numer - m\nAby zakończyć - q")
while(True):
    znak = input()
    if znak == "w":
        print(ksiazka)
    elif znak == "a":
        print("Podaj imię i nazwisko nowej osoby:")
        dane = input()
        print("Podaj jej numer telefonu:")
        numer = input()
        ksiazka[dane] = numer
        print("Dodano!")
    elif znak == "r":
        print("Podaj imię i nazwisko osoby którą chcesz usunąć:")
        osoba = input()
        if dane in ksiazka:
            del (ksiazka[osoba])
            print("Usunięto!")
        else:
            print("Nie ma takiej osoby")
    elif znak == "m":
        print("Której osoby numer chcesz zmienić?")
        dane2 = input()
        print("Podaj nowy numer telefonu:")
        numer2 = input()
        ksiazka[dane2] = numer2
        print("Zmieniono!")
    elif znak == "q":
        print("Koniec!")
        break
    else:
        print("Nieprawidłowy znak")