#Program to find out the factorial of a number

def Factorial(n):
	fact = 1
	for i in range(1, n+1):
		fact *= i
	print(1 / fact)	


number = int(input("Enter the number for which you want the inverse of factorial"))
Factorial(number)