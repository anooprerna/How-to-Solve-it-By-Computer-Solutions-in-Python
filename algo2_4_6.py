#Design an algorithm that evaluates all coefficients of x for a given value of n. Binomial theory application for (x+1)^n
import math

def binomial(n):
	
	r = 0
	while(n >= r):
		coefficient = math.factorial(n)/(math.factorial(r) * math.factorial(n - r))
		print("The coefficient of x power", n - r, "is ", coefficient)
		r += 1
   
n = int(input("Binomial Theory - Enter the value for n: "))
if n <= 0:
	print("Sweetum, Please enter a value greater than 0")
	
else:
	binomial(n)
 