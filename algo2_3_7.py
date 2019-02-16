#Program to print first n terms of the series 1, -1, 1, -1, 1, -1, 1, -1.....

def nseries(n):
	number = 1
	nnum = -1
	for i in range(n):
		if i % 2 == 0:
			print(number, end = " ")
		else:
			print(nnum, end = " ")
	
		
number = int(input("Enter a number for which you want the series of numbers"))
nseries(number)
