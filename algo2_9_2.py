c = int(input("Alright, let's enter some number!"))
lists = []
while c != 0:
    r = c%10
    c = c//10
    a = r + 48
    #Decimal to ASCII
    a_n = chr(a)
    lists.append(a_n)
print(''.join(reversed(lists)))
print(type(''.join(reversed(lists))))