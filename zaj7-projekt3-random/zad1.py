import random

suma = 10

for i in range (10):
    suma = suma + random.randint(-10, 10)

print("Twój stan portfela po 10 dniach to:",suma)