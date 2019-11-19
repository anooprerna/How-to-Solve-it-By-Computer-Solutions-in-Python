number = int(input("Enter a number to convert\n"))
base = int(input("Enter the base\n"))
result = ""
while number != 0:
    remainder = number % base
    number = number // base
    result = str(remainder) + result
print("The representation of number to the base", base, "is", result)