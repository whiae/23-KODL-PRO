import random
class Samochod():

    def __init__(self):
        self.pojemnosc_baku = random.randint(1,100)
        self.spalanie = random.randint(1,20)
        self.droga = 0

    def jazda(self, droga):
        if self.pojemnosc_baku >= self.spalanie:
            self.pojemnosc_baku -= self.spalanie
            self.droga += 1
        else:
            self.pojemnosc_baku = 0

auto1 = Samochod()
auto2 = Samochod()

while auto1.pojemnosc_baku > 1 and auto2.pojemnosc_baku > 1:
    auto1.jazda(auto1.spalanie)
    auto2.jazda(auto2.spalanie)
    #print(auto1.pojemnosc_baku, auto1.spalanie, auto1.droga)
    #print(auto2.pojemnosc_baku, auto2.spalanie, auto2.droga)
    if auto1.spalanie > auto1.pojemnosc_baku and auto2.spalanie < auto2.pojemnosc_baku:
        auto2.pojemnosc_baku = auto2.pojemnosc_baku/2
        auto1.pojemnosc_baku = auto1.pojemnosc_baku + auto2.pojemnosc_baku
        print("Podzielono sie benzyna z drugiego auta!")
    if auto2.spalanie > auto2.pojemnosc_baku and auto1.spalanie < auto1.pojemnosc_baku:
        auto1.pojemnosc_baku = auto1.pojemnosc_baku/2
        auto2.pojemnosc_baku = auto2.pojemnosc_baku + auto1.pojemnosc_baku
        print("Podzielono sie benzyna z pierwszego auta!")
print("Samochod pierwszy przejechał:", auto1.droga, "km")
print("Samochod drugi przejechał:", auto2.droga, "km")
