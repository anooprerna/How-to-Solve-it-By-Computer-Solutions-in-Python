number = int(input("Enter a decimal number. Let's convert it to BCD!"))
result = []
while number != 0:
    remainder = number % 10
    number = number // 10

    if remainder == 0:
        result.append("0000")
    elif remainder == 1:
        result.append("0001")
    elif remainder == 2:
        result.append("0010")
    elif remainder == 3:
        result.append("0011")
    elif remainder == 4:
        result.append("0100")
    elif remainder == 5:
        result.append("0101")
    elif remainder == 6:
        result.append("0110")
    elif remainder == 7:
        result.append("0111")
    elif remainder == 8:
        result.append("1000")
    elif remainder== 9:
        result.append("1001")


print(result)

for i in reversed(result):
    print(i, end='')
