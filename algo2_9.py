c = input("Alright, let's enter some number and we will convert it to decimal!")
size = len(c)
d = 0
i = 0
while i < size:
    #print("Character",c[i])
    a = ord(c[i])
    #print("ASCII", a)
    x = a - 48
    #print("Decimal", x)
    d = (d*10) + x
    #print("Printing D", d)
    i+=1
print(d)