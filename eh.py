# def numbers(amount, deposit):
#     number1 = amount
#     numb2 = deposit

def cal(amount):
    thou = amount // 1000
    thou1 = amount % 1000

    lima = thou1 // 500
    liman = thou1 % 500

    hund = liman // 100
    hunde = liman % 100

    fift = hunde // 50
    fifty = hunde % 50

    twent = fifty // 20
    twenty = fifty % 20

    te = twenty // 10
    ten = twenty % 10

    fiv = ten // 5
    five = ten % 5

    on = five // 1


print(thou)
print(lima)
print(hund)