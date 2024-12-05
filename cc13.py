for x in range(1,6):
    for z in range(1,x +1):
        print(" ", end=" ")
    for y in range(10,x,-1):
        print(x, end=" ")
    for a in range(11, x, -1):
        print(x, end=" ")
    print()