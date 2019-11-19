
lst = []
n = int(input("Enter number of elements : "))
print("Please enter", n, "numbers then!")

for i in range(0, n):
    ele = int(input())

    lst.append(ele)
print(lst)

Number = 0
x = n-1
j = 0
while x >= 0:
    Number = Number + (lst[j]*(10**(x)))
    print(lst[j])

    j+=1
    x-=1

print(Number)






