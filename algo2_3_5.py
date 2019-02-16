#Program to calculate sum of first n series. 

n_number = int(input("Enter a number"))
number = n_number

sum = 0

while number > 0:
	sum += number
	number -= 1
	
print("The sum of natural numbers up to ", n_number, "is ", sum )



#Sum of first n odd numbers
odd = (n_number * 2) - 1
odd_sum = 0

while (odd > 0):
	odd_sum += odd
	odd -= 2
print("The sum of first ", n_number, "odd numbers is ", odd_sum)


#Sum of first n even numbers
even = (n_number * 2)
even_sum = 0

while (even > 1):
	even_sum += even
	even -= 2
print("The sum of first ", n_number, "even numbers is ", even_sum)


#Sum of fractions
f_number = n_number
fraction = 0
while f_number > 0:
	fraction += 1/f_number
	f_number -= 1

print("Sum of fractions ", fraction)







