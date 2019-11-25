c = input("Enter something! I will tell you if you have numbers in it or not!")
for i in c:
    if ord(i) >=48 and ord(i) <=58:
        print("YAY! You have number in it!")
        break
    else:
        continue