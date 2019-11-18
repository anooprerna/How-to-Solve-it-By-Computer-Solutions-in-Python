import math
n = int(input("How many terms?!"))
f = n + 1
n1 = 0
n2 = 1
count = 2
fib = []

if f <= 0:
   print("Please enter a positive integer")
elif f == 1:
   print("Fibonacci sequence upto",f,":")
   print(n1)
else:
   print("Fibonacci sequence upto",f,":")
   fib.append(n1)
   fib.append(n2)
   while count < f:




       n1 = n1 + n2
       n2 = n1 + n2

       count += 2
       if count >= f:
           if f % 2 == 0:
               print(n1, n2, end=' ')
               fib.append(n1)
               fib.append(n2)
           else:
               fib.append(n1)

       else:
           fib.append(n1)
           fib.append(n2)

print(fib)
s = 0
i = 0
while s <= f:
    try:
        sum = math.factorial(fib[i]) + math.factorial(fib[i+1])
        print(sum)
        i += 1
        s += 1

    except:
        continue




