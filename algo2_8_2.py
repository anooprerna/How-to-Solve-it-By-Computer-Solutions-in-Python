binary = input("Enter a number in binary format")
size = len(binary)
decimal = 0
x = size - 1
i = 0
while x >= 0:
    decimal = decimal + (int(binary[x]) * (2**i))
    i+=1
    x-=1
print(decimal)


result = ""
while decimal != 0:
    remainder = decimal % 8
    decimal = decimal // 8
    result = str(remainder) + result
print("The representation of number to the base", 8, "is", result)
