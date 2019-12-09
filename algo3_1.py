n = int(input("Enter a number, I will calculate the square root of that number! NOT USING BUILT IN FUNCTION OF COURSE!"))
e = 0.00000001

g1 = n/2

while True:
    g2 = (g1 + n/g1)/2
    if abs(g1 - g2) < e:
        break
    g1 = g2
print("Sqaure root is", g2)

