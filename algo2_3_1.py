print("Enter the numbers whose average is to be returned")

numbers = [int(x) for x in input().split()]
length = len(numbers)
sum = 0

for i in numbers:
	sum += i
	


print("Average is ", sum/length)

