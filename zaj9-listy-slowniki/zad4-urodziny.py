lista = [("Ania", "1997-06-02"),("Daria", "1999-10-22"),("Łukasz", "1997-06-24"),("Agata", "1998-11-16")]

lista.sort()
print(lista)

lista.sort(key=lambda x: x[1])
print(lista)
