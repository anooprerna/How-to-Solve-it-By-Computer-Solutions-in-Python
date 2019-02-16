print("Enter the numbers whose sum is to be returned")

numbers = [int(x) for x in input().split()]
length = len(numbers)
sum = 0
#sum_sqrt = 0
#h_m = 0
#reci = 0

for i in numbers:
	sum += i
	#sum_sqrt += i**2
	#reci += (1/i)
	
#h_m = length/reci

print(sum)
#print(sum_sqrt)
#print(reci)
#print(h_m)
#print("Average is ", sum/length)

