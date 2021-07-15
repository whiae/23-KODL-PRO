foodlog = {"zupa pomidorowa":"11:30", "gołąbki":"12:00", "pierogi":"15:00", "naleśniki":"17:00"}

print("Aby wyświetlić cały foodlog - w\nAby dodać log - a\nAby usunąć log - r\nAby wyświetlić pojedynczy element - o\nAby zakończyć - q")
while(True):
    znak = input()
    if znak == "w":
        print(foodlog)
    elif znak == "a":
        print("Podaj nazwę dania:")
        ate = input()
        print("Podaj czas w formacie HH:MM:")
        time = input()
        foodlog[ate] = time
        print("Dodano!")
    elif znak == "r":
        print("Podaj nazwę dania które chcesz usunąć:")
        dnate = input()
        if dnate in foodlog:
            del (foodlog[dnate])
            print("Usunięto!")
        else:
            print("Nie ma takiego dania w foodlogu!")
    elif znak == "o":
        print("Które danie chcesz wyświetlić?")
        dish = input()
        if dish in foodlog:
            print(foodlog[dish])
        else:
            print("Nie ma takiego dania w foodlogu!")
    elif znak == "q":
        print("Koniec!")
        break
    else:
        print("Nieprawidłowy znak")