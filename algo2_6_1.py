import math

def Fibonacci():
    n1 = int(input("Enter the first Fibonacci Number"))
    n2 = int(input("Enter the second Fibonacci Number"))
    diff = abs(n1 - n2)
    print("Difference of numbers is", diff)
    minimum = min(n1, n2)
    print("Minimum of two numbers is", minimum)
    if diff > minimum:
        print("Numbers are not consecutive in Fibonacci series!")
    else:
        return n1 + n2

print("The resulting Fibonacci Number is", Fibonacci())
