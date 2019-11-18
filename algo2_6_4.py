import math
n1 = int(input("First Fibonacci number please!\n"))
n2 = int(input("Second Fibonacci number please!\n"))
diff = abs(n1-n2)
print("Difference of numbers is", diff)
minimum = min(n1, n2)
print("Minimum of two numbers is", minimum)
if diff > minimum:
    print("Numbers are not consecutive!")
else:
    print("Numbers are two consecutive numbers of Fibonacci series")
