import random

l1 = random.randint(1,49)
l2 = random.randint(1,49)

while l2 == l1:
    l2=random.randint(1,49)
l3=random.randint(1,49)

while l3 == l1 or l3 == l2:
    l3=random.randint(1,49)
l4 = random.randint(1,49)

while l4 == l1 or l4 == l2 or l4 == l3:
    l4 = random.randint(1, 49)
l5 = random.randint(1, 49)

while l5 == l1 or l5 == l2 or l5 == l3 or l5 == l4:
    l5 = random.randint(1, 49)
l6 = random.randint(1, 49)

while l6 == l1 or l6 == l2 or l6 == l3 or l6 == l4 or l6 == l5:
    l6 = random.randint(1, 49)
print("Wylosowane liczby to:",l1, l2, l3, l4, l5, l6)
