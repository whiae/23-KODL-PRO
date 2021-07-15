import random
import time

przyslowia = ["Bez pracy nie ma kołaczy.", "Darowanemu koniowi w zęby się nie zagląda.", "Fortuna kołem się toczy.", "Nie chwal dnia przed zachodem słońca.", "Lepszy wróbel w garści niż gołąb na dachu."]
print("Losuję...")
time.sleep(1)
losowe = random.choice(przyslowia)
print(losowe)