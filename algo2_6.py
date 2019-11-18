#Generation of Fibonacci Sequence
#
# nterms = int(input("How many terms of fibonacci sequence do you want?!\n"))
#
# # first two terms
# n1 = 0
# n2 = 1
# count = 0
#
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence upto",nterms,":")
#    while count < nterms:
#        print(n1,end='  ')
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1
#
# #
#
#
# #
#
#Generation of Fibonacci Sequence. IT doesn't work when nterms is odd!

nterms = int(input("How many terms of fibonacci sequence do you want?!\n"))

# first two terms
n1 = 0
n2 = 1
count = 2

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   print(n1, n2, end=' ')
   while count < nterms:




       n1 = n1 + n2
       n2 = n1 + n2

       count += 2
       if count >= nterms:
           if nterms % 2 == 0:
               print(n1, n2, end=' ')
           else:
               print(n1)
       else:
           print(n1, n2, end=' ')








