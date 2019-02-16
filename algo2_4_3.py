#Design an algorithm to determine whether or not a given number n is a factorial number or not. 

def determine_fact(n):
	if n == 0:
		print("Well, it's 1 for 0!")
		exit
	elif n < 0:
		print("Factorial doesn't exist for a negative number!")
		exit	
	else:
		fact = 1
		for i in range(1, n+1):
			fact *= i
			if fact < n:
				continue
			elif fact == n:
				print("What a beauty! It's a factorial number, dude! It's", i, "!")
				break
			else:
				print("Sorry, it's not a factorial number. It takes a lot to be one!")
				break


number = int(input("Enter a number to determine if it's a factorial number or not"))
determine_fact(number)