number = int(input("Enter a number to convert into octal: "))
result = ""
while number != 0:
    remainder = number % 8
    number = number // 8
    result = str(remainder) + result
print("The octal representation is", result)