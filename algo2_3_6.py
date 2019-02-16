#Program to print first n terms of the series 1, 2, 4, 8, 16, 32.... Without using multiplication

def nseries(n):
	
	first = 1
	next = 1
	while (n >= 1):
		print(next)
		next += first
		first = next
		n -= 1
		
number = int(input("Enter a number for which you want the series of numbers"))
nseries(number)
