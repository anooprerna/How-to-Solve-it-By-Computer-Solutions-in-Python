#Only n-1 additions to sum n numbers

print("Enter the numbers whose sum is to be returned")

numbers = [int(x) for x in input().split()]
length = len(numbers)
sum = numbers[0] + numbers[1]

num_add = 1

del numbers[0]
del numbers[0]

if length >= 3: 
	for i in numbers:
		sum += i
		num_add += 1
		
print("Sum is ",sum)
print("Number of additions are ", num_add)

