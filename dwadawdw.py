for x in range(11,0,-1):
    for z in range(1,x +1):
        print(" ", end=" ")
    for y in range(11,x,-1):
        print("*", end=" ")
    for a in range(11, x, -1):
        print("*", end=" ")
    print()

for x in range(1,11):
    for z in range(1,x+1):
        print(" ", end=" ")
    for y in range(11,x,-1):
        print("*", end=" ")
    for a in range(22,x,-1):
        print("*", end=" ")
    print()
