Number = int(input("Please Enter any Number: "))
Sum = 0
while(Number > 0):
    Remainder = Number %10
    Sum = Sum + Remainder
    Number = Number //10

print("\n Sum of digits of entered number is",Sum)