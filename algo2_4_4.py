#Design an algorithm which, given some integer n, finds the largest factorial number present as a factor in n.	

def Function(n):
	number = n
	for i in range(1, n+1):
		if (n % i) == 0:
			n /= i
			factorial = i
			continue
		else:
			factorial = i -1			
			break
	
	fact = 1
	
	for i in range(1, factorial+1):
		fact *= i
	
	print("The biggest factorial number as a factor of", number, "is", fact)
		
		
	

number = int(input("Enter a number greater than 0"))
Function(number)