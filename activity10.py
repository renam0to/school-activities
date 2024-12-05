username = input("Please enter your full name: ")

ifDLL = input("Are you a current student of DLL? (yes / no): ")

if ifDLL.lower() == "yes":
	print("Welcome to the DLL BSIT Scholarship Form")
	isGG = input("Are you from Brgy Ibabang Iyam (yes / no): ")
	
	if isGG.lower() == "yes":
		print("Please fillup the second form ")
		isLevel = input("What is youre current year level right now in DLL\nF-Freshmen\nS-Sophomore\nJ-Junior\nR-Senior\nPlease input your answer: ")

		if isLevel.lower() == 'f':
			print("Hi Freshmen!")
		elif isLevel.lower() == 's':
			print("Hi Sophomore!")
		elif isLevel.lower() == 'j':
			print("Hi Junior!")
		elif isLevel.lower() == 'r':
			print("Hi Senior!")
		else:	
			print("Invalid Choice")
		isNeeded = input("Do you need this scholarship (yes / no): ")

		if isNeeded.lower() == "yes":	
			print("Scholarship Granted")
		else:
			print("Thanks for stopping by")
else:
    print("A student must be around these premises..")




























