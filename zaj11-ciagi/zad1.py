print("Podaj pierwszy ciąg:")
pierwszy_ciag = input()
print("Podaj drugi ciąg:")
drugi_ciag = input()

print(pierwszy_ciag, drugi_ciag)

roznice = ""

for i in range(len(pierwszy_ciag)):
        if pierwszy_ciag[i] != drugi_ciag[i]:
            roznice = roznice + pierwszy_ciag[i] + drugi_ciag[i]

print("Znaki którymi różnią się oba ciągi to:",roznice)