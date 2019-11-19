Number = int(input("Please Enter any Number: "))
c = 0
while(Number > 0):
    Remainder = Number %10

    Number = Number //10
    c+=1

print("Number of digits is =", c)