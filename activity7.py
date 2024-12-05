gold = 0
name = input("name:")

isgold = input("IS THE MINERAL GOLD? {Y/N}").upper().strip()

if isgold == "YES":
    gold += 1
    print(f"Hi! {name}, Your total number of Gold is: {isgold}")