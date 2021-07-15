import random
import time

print("== START ==")
i = 6

while i > 0:
    liczba = random.randint(1,49)
    time.sleep(1)
    print("Wylosowana liczba to:", liczba)
    i = i - 1

##for i in range(6):