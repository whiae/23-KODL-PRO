slownik = {"dog":"pies", "cat":"kot", "mouse":"mysz", "fish":"ryba", "fox":"lis"}

print("Jakie słowo przetłumaczyć?")
slowo = input()
if slowo in slownik:
    print(slownik.get(slowo))
else:
    print("Nie ma tego słowa w słowniku")