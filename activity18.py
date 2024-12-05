col=eval(input("number of columns sire: "))

for x in range(1,11):
    for z in range(1,col +1):
        print(f"{x} * {z} = {x * z}", end="\t")
    print()
