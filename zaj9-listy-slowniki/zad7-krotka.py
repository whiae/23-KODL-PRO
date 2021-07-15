krotka = (1,2,3,4,5,6,7,8,9,10)
suma = 0
min = 100
max = 0

for i in krotka:
    suma = suma + i
    if min > i:
        min = i
    elif max < i:
        max = i

srednia = suma / 10
print(min,max,srednia)