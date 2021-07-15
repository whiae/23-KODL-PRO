liczba = 0
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            print(str(i) + str(j) + str(k))
            if i == 4:
                liczba = liczba + 1
        if j == 4:
            liczba = liczba + 1
    if k == 4:
        liczba = liczba + 1
print("Ilosc wystapien liczby cztery: " + str(liczba))
