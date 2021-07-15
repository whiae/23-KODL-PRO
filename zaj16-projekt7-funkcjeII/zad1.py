def binegacja(P,Q):
    if P == Q == 0:
        return True
    else:
        return False

print("P = 0, Q = 0: " + str(binegacja(0,0)))
print("P = 0, Q = 1: " + str(binegacja(0,1)))
print("P = 1, Q = 0: " + str(binegacja(1,0)))
print("P = 1, Q = 1: " + str(binegacja(1,1)))