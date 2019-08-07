#Design an algorithm to find the sum of the first n terms of the series
#fs = 0! + 1! + 2! + 3! + ..... + n!
def Factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


n = int(input("Enter the value of n to calculate the sum of the series!"))
sum = 0
for i in range(n + 1):
    sum = sum + Factorial(i)
print(sum)