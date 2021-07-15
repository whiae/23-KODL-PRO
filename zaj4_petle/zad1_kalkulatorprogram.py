print("Podaj pierwsza liczbe:")
a = int(input())
print("Podaj druga liczbe:")
b = int(input())

dodawanie = a+b
odejmowanie = a-b
mnozenie = a*b
dzielenie = a/b

while True:
    print("Dodawanie - klawisz \"d\"")
    print("Odejmowanie - klawisz \"o\"")
    print("Mnozenie - klawisz \"m\"")
    print("Dzielenie - klawisz \"z\"")
    print("Aby zakonczyc wcisnij klawisz \"q\"\n")
    znak = input()
    if znak == "d":
        print("Wynik: " + str(dodawanie) +"\n")
    elif znak == "o":
        print("Wynik: " + str(odejmowanie) +"\n")
    elif znak == "m":
        print("Wynik: " + str(mnozenie) +"\n")
    elif znak == "z":
        print("Wynik: " + str(dzielenie) +"\n")
    elif znak == "q":
        break
else:
    print("Nieprawidlowy znak!")
