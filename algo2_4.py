#Program to find out the factorial of a number

def Factorial(n):
	fact = 1
	for i in range(1, n+1):
		fact *= i
	print(fact)	


number = int(input("Enter the number for which you want the factorial"))
Factorial(number)