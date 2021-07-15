print("Witaj w programie! Co chcesz zrobić?\n")
print("Wyjście z programu - klawisz q")
print("Wyświetl informacje o autorze - klawisz a")
print("Zadanie 1 - klawisz 1")
print("Zadanie 2 - klawisz 2")
print("Zadanie 3 - klawisz 3")

while True:
    znak = input()
    if znak == "q":
        print("Do zobaczenia!")
        break
    elif znak == "a":
        print("Weronika Szczegodzińska")
        print("Kognitywistyka, I rok")
    elif znak == "1":
        suma = 0
        for i in range(-50,51):
          if i%2 != 0:
            suma = suma + i
        print("Suma liczb: " + str(suma))
    elif znak == "2":
        i = -50
        while i>=-50 and i <= 0:
            if i%3 == 0:
                if i%2 == 0:
                    print(i, "parzysta")
                else:
                    print(i, "nieparzysta")
            i = i + 1
    elif znak == "3":
        for i in range(0,151):
            if i%3 == 0:
                if i%2 == 0:
                    print(i, "parzysta")
                else:
                    print(i, "nieparzysta")
    else:
        print("Nieprawidłowy znak!")
