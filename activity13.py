number = 0
number = eval(input("input a number: "))
for i in range(number,0,-1):
	number *= i

print(f"factored to {number}")
