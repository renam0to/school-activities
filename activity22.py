def activity1():
    print("\t\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t\t      * * *\n\t\t\t\t\t\t\t\t\t\t    * * * * *\n\t\t\t\t\t\t\t\t\t\t      * * *\n\t\t\t\t\t\t\t\t\t\t\t*")

def activity2():
    num1 =eval(input("input a number: "))
    num2 =eval(input("input another number: "))
    print("the floor division of ",num1, " and ",num2," is",num1 // num2)

def activity3():
    name=input('Hello! Please type your name here: ')
    dob=input('date of birth(MM/DD/YYYY): ')
    age=input('age: ')
    email=input('email address: ')
    language=input('known languages: ')
    occupation=input('occupation: ')

    print('\n')
    print('Hello!',name)
    print('Your biodata:')
    print('\tDOB:', dob)
    print('\tAGE:',age)
    print('\tEMAIL:',email)
    print('\tLANGUAGES:',language)
    print('\tOCCUPATION:',occupation)

def activity4():
    number1 = eval(input("input thy number >> "))
    number2 = eval(input("input thy number >> "))

    answer1 = number1 + number2
    answer2 = number1 / number2
    answer3 = number1 - number2
    answer4 = number1 * number2
    answer5 = number1 // number2


    print ("The sum of", number1,"and", number2, "is", answer1)
    print ("The division of", number1,"and", number2, "is", answer2)
    print ("The differences of", number1,"and", number2, "is", answer3)
    print ("The quotient of", number1,"and", number2, "is", answer4)
    print ("The floor division of", number1,"and", number2, "is", answer5)

def activity5():
    temp = eval(input("input Temperature Farenheit: "))
    cel = (temp - 32 ) * 5/9
    print(f"The conversion of {temp} degrees Farenheit is {round(cel,2)} degrees Celius.")

def activity6():
    x = 5
    print(x)

    x += 10
    print(x)

    x =+ 15
    print(x)

    x =- 10
    print(x)

def activity7():
    gold = 0
    name = input("name:")

    isgold = input("IS THE MINERAL GOLD? {Y/N}").upper().strip()

    if isgold == "YES":
        gold += 1
        print(f"Hi! {name}, Your total number of Gold is: {isgold}")

def activity8():
    pre = eval(input(" your prelim "))
    mid = eval(input(" your midterm "))
    semi = eval(input(" your semi "))
    final = eval(input(" your final "))
    quiz = eval(input(" your quiz "))
    project = eval(input(" your project "))

    fg = (pre * .15) + (mid * .15) + (semi * .15) + (final * .15) + (quiz * .25) + (project * .15)  

    if fg >= 65:
    
        print("congrats you passed!")
    elif fg >= 100:
        print("too high!! the grades must be under 100")
        
    else:
        print("you failed..")

    print("you may leave the room, goodbye")


def activity9():
    age = eval(input("your age: "))

    if age >= 60 and age <=100: 
        print('Youre currently in Senior Age')
    elif age >= 46 and age <= 59:
        print('Youre currently in Post adulthood')
    elif age >=  32 and age <= 45:
        print('Youre currently in Mid Adulthood')
    elif age >= 19 and age <= 31:
        print('Youre currently in Early Adulthood')
    elif age >= 14 and age <= 18:
        print('Youre currently in Teenager')
    elif age >=8 and age <=13:
        print('Youre currently in Pre-Teen')
    elif age >= 1 and age <=7:
        print('Youre currently in Toddler')

    else:
        print('input a real number')


def activity11():
    for i in range(1,11):
        print("Hello world!")
        print("Happy Foundation")
        single = False
        print(f"{single}, That I'm Single")

def activity12():
    for i in range(11,0,-1):
	    print(i)
def activity13():
    number = 0
    number = eval(input("input a number: "))
    for i in range(number,0,-1):
        number *= i

    print(f"factored to {number}")

def activity14():
    for x in range(0,11):
    print(x, end = " ")
    for y in range(0,2 ):
        print("*", end = " ")
    print()

def activity15():
    






act = eval(input("CHOOSE ANY ACTIVITIES GIVEN:"))
if act == 1:
    activity1()
elif act == 2:
    activity2()
if act == 3:
    activity3()
elif act == 4:
    activity4()
else:
    print("invalid..")