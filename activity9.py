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