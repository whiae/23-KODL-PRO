def mnozenie_list(lista1,lista2,dlugosc):
    wynik = []
    for i in range(dlugosc):
        wynik.append(lista1[i]*lista2[i])
    return wynik

przyklad1 = [1,2,3,4]
przyklad2 = [2,4,6,8]
print("Wynik mnozenia list " + str(przyklad1) + " oraz " + str(przyklad2) + "\nto: " + str(mnozenie_list(przyklad1,przyklad2, 4)) + "\n")

dwucyfrowe1 = [10,20,30,40,50,60]
dwucyfrowe2 = [20,40,60,80,90,100]
print("Wynik mnozenia list " + str(dwucyfrowe1) + " oraz " + str(dwucyfrowe2) + "\nto: " + str(mnozenie_list(dwucyfrowe1,dwucyfrowe2, 6)) + "\n")

dluzsze1 = [1,2,3,4,5,6,7,8,9,0]
dluzsze2 = [2,4,6,8,10,12,14,16,18,20]
print("Wynik mnozenia list " + str(dluzsze1) + " oraz " + str(dluzsze2) + "\nto: " + str(mnozenie_list(dluzsze1, dluzsze2, 10)) + "\n")