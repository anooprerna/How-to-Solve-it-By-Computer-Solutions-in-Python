df = float(input("Enter a decimal fraction"))
b = ''
while df != 0:
    df *= 2
    print(df)
    if df >= 1:
        b+='1'
        print(1)
        df -= 1
    else:
        b+='0'
        print(0)
print("Binary version of decimal is 0." + b)
