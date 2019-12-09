import random
n = int(input("Enter a number, I will calculate the square root of that number! NOT USING BUILT IN FUNCTION OF COURSE!"))
e = 0.0000000001
r1 = random.randint(0, n)
print(r1)
sub_c = 1
add_c = 0.1
while (n - (r1**2)) < e:

    if r1**2 > n:
        r1 -= sub_c
    else:
        r1 += add_c
        sub_c /= 100
        add_c /= 100

print(r1)

