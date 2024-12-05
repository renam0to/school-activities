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