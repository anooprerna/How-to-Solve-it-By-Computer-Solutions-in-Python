#Lucas Series

Terms = int(input("Emter the number of terms you want for Lucas Series!\n"))
First = 1
Second = 3
Count = 0

if Terms <= 0:
   print("Please enter a positive integer")
elif Terms == 1:
   print("Lucas sequence upto",Terms,":")
   print(First)
else:
    print("Lucas sequence upto", Terms, ":")

    while Count < Terms:
        print(First, end=' ')
        Next = First + Second
        First = Second
        Second = Next
        Count += 1
