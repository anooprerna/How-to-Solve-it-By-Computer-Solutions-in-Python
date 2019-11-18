nterms = int(input("How many terms of this new sequence do you want?!\n"))


n1 = 0
n2 = 1
n3 = 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Sequence upto",nterms,":")
   print(n1)
else:
   print("Sequence upto",nterms,":")
   while count < nterms:
       print(n1,end='  ')
       nth = n1 + n2 + n3
       n1 = n2
       n2 = n3
       n3 = nth
       count += 1
