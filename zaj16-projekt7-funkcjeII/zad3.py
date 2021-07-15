def bez_nieparzystych(lista):
    for liczba in lista[:]:
        if liczba % 2 != 0:
            lista.remove(liczba)
        else:
            continue
    return lista

przyklad1 = [1,2,3,4,5,6,7,8,9,10]
print("Lista " + str(przyklad1) + " po usunieciu liczb nieparzystych: " + str(bez_nieparzystych(przyklad1)) + "\n")

przyklad2 = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
print("Lista " + str(przyklad2) + " po usunieciu liczb nieparzystych: " + str(bez_nieparzystych(przyklad2)) + "\n")

przyklad3 = [11,33,55,77,99]
print("Lista " + str(przyklad3) + " po usunieciu liczb nieparzystych: " + str(bez_nieparzystych(przyklad3)) + "\n")