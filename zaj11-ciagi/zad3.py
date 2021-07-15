print("Wpisz ciąg znaków:")
ciag = input()

lista = list(ciag)
nowy_ciag = []

for i in range(len(lista)):
    if i % 2 == 0:
        nowy_ciag += lista[i]
    else:
        nowy_ciag += "X"
    i = i+1

string_ciag = "".join(nowy_ciag)
print(string_ciag)