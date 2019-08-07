#Design an algorithm that evaluates sin(x) as defined by infinite series expansion
#sin(x) = (x/1!) - ((x^3)/3!) + ((x^5)/5!) - ((x^7)/7!).......

import math

def sin(x,n):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        
        sine = sine + ((y**(2*i+1))/math.factorial(2*i+1))*sign
    return sine

x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))
print(sin(x,n))
