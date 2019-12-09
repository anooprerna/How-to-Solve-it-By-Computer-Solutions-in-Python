import random
e = 0.000001
n = int(input("How many numbers buddy?"))
list_of_n = []
print("Alright, keep entering the numbers")
for i in range(0, n):
    numbers = int(input())

    list_of_n.append(numbers)

print(list_of_n)
product = 1
for i in list_of_n:
    product *= i
print(product)

r1 = random.randint(0, product)
sub_c = 1
add_c = 0.1
while (product - (r1**n)) < e:

    if r1**n > product:
        r1 -= sub_c
    else:
        r1 += add_c
        sub_c /= 100
        add_c /= 100

print(r1)





#
# e = 0.00000001
#
# g1 = n/2
#
# while True:
#     g2 = (g1 + n/g1)/2
#     if abs(g1 - g2) < e:
#         break
#     g1 = g2
# print("Sqaure root is", g2)
#
#
#
# #