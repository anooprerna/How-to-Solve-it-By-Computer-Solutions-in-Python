#Design an algorithm that evaluates sin(x) as defined by infinite series expansion
#cos(x) = 1 - ((x^2)/2!) + ((x^4)/4!) - ((x^6)/6!).......


import math


def cos(x, n):
    cosine = 0
    for i in range(1, n + 1):
        sign = (-1) ** i
        pi = 22 / 7
        y = x * (pi / 180)

        cosine = cosine + (((y ** (2 * i)) / math.factorial(2 * i)) * sign)
        cosine_final = 1 + cosine


    return cosine_final

x = int(input("Enter the value of x in degrees:"))
n = int(input("Enter the number of terms:"))
print(cos(x, n))

