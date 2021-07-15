import random

print("Aby rzucić wciśnij r\nAby zakończyć program wciśnij q")
while(True):
    znak = input()
    if znak == "r":
        wylosowana = random.randint(1,6)
        print("Wylosowana liczba to:", wylosowana)
    elif znak == "q":
        print("Koniec pogramu!")
        break