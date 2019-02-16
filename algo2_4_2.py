#For a given x and n, design an algorithm to calculate x**n / n!


def Function(x, n):
	fact = 1
	for i in range(1, n+1):
		fact *= i
	final = (x ** n) / fact
	print("The value is", final)

x = int(input("Enter the values for x"))
n = int(input("Enter the values for n"))
Function(x, n)