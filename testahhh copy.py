inp=eval(input("number of triangles sire: "))
for x in range(1,5):
    for a in range(1, inp +1):
        for o in range(1,x +1):
            print("*", end=" ")
        for l in range(5,x,-1):
            print(" ", end=" ")
        print(end=" ")
    print()

    