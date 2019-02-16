#Design an algorithm to simulate multiplication by addition. Your program should accept as input two integers (They may be zero, positive or negative).

def multiply(x,y): 
  
   
    if(y == 0): 
        return 0
  
      
    if(y > 0 ): 
        return (x + multiply(x, y - 1)) 
  
    
    if(y < 0 ): 
        return -multiply(x, -y) 
      
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(multiply(x, y))
 