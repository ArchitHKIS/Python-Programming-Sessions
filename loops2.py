low = eval(input("What is the lower bound? (inclusive)\n"))
up = eval(input("What is the upper bound? (inclusive)\n"))
if low == 0:
    print(low)
for x in range(low, up+1):
    if x % 5 != 0:
        if x % 7 == 0:
            print(x)
