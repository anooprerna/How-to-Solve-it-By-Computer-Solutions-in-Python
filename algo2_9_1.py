
c = input("Alright, let's enter some number and we will convert it to decimal!")
size = len(c)
d=0
n=0
j=0
for i in c:
    a = ord(i)
    #When you come across decimal point!
    if a == 46:
        break
    d+=1

f = size - d - 1
print(type(c))






while j < d:
#ASCII VALUE buddy - ord() function
    a = ord(c[j])

    x = a - 48

    n = (n*10) + x

    j+=1

h = size - f
l=0

p = -1
while h < size:

    a = ord(c[h])


    x = a - 48

    r = x*(10**(p))

    l = l + r

    h+=1
    p-=1

print(n+l)
print(type(n+l))