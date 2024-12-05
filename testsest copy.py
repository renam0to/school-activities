for i in range(1,6):
    for w in range(1,6):
        print("`~.->==>", end=" ")
    for z in range(1, i+1):
        print(" ", end="")

    for d in range(6,i,-1):
        print("*", end=" ")
    print()