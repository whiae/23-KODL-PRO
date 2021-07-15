import random
import time

print("== START ==")
wylosowana = 0

while(True):
    if wylosowana <= 91:
        wylosowana = random.randint(0, 99)
        print(wylosowana)
        time.sleep(1)
    else:
        print("Liczba większa niż 90!")
        break