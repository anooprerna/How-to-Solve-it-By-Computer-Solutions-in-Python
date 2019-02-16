#Program to find out the sum of the first n (n>=1 )numbers of the series s = 1 -3 +5 -7 +9 -11, 13, -15....

def series_sum(n):
	sum = 0
	counter = 1
	for i in range(1, 2*n, 2):
		if counter % 2 == 0:
			sum += (-i)
		else:
			sum += i
		counter += 1
	print("The sum is", sum)


number = int(input("Enter the number till when you want the sum"))
series_sum(number)