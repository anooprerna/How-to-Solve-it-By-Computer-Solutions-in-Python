#The exponential growth constant e is characterized by the expression
#1/0! + 1/1! + 1/2! + 1/3! + ..... + 1/n!
#Devise an algorithm to compute e to n terms

def Factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


n = int(input("Enter the value of n to calculate the value of e to n terms!"))
sum = 0
for i in range(n + 1):
    sum = sum + 1/Factorial(i)
print(sum)