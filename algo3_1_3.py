import random
n = int(input("Enter a number, I will do some magic!"))
e = 0.0000000001
r1 = random.randint(0, n)
print(r1)
# sub_c = 1
# add_c = 0.1
while (n - (r1**2)) < e:

    if r1**2 > n:
        r1 -= 1
    else:
        break
        # sub_c /= 100
        # add_c /= 100

print("The magical number is", r1+1)

