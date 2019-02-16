#Sum of squares of n numbers. 

print("Enter the numbers whose sum of squares is to be returned")

numbers = [int(x) for x in input().split()]

sum = 0

for i in numbers:
		sum += i * i

		
print("Sum of squares is ", sum)


