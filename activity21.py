countin = True
count = 0

while countin == True:
    name= input("whats yar name:").upper().strip()

    if name == "STOP":
        print("The loop has stopped..")
        print(f"You have entered {count} number of names")
        break
    else:
        count += 1
        continue

    

