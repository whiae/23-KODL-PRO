print("Podaj wyrażenie do sprawdzenia:")
lancuch = input()
odwrocony = ""

for i in range(len(lancuch)-1, -1, -1):
    odwrocony += (lancuch[i])

if (lancuch.replace(" ","").lower() == odwrocony.replace(" ","").lower()):
    print("To jest palindrom!")
else:
    print("To nie jest palindrom!")