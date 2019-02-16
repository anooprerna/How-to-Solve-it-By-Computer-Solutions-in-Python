#Program to calculate harmonic mean of n numbers.


print("Enter the numbers - I will get you the harmonic mean")
numbers = [int(x) for x in input().split()]
length = len(numbers)

denom_sum = 0

for i in numbers:
		denom_sum += 1/i

harmonic_mean =  length/denom_sum
		
print("Harmonic mean is ", harmonic_mean)


