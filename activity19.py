from ast import Continue


varia = True
while varia == True:
    name=input("your name dawg: ")
    print("wassuh",name)
    print("Type 'STOP' to terminate the loop")

    if name.lower() == "stop":
        print("Process has terminated")
        break
        varia = False
    else:
        continue