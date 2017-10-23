lowerBound = eval(input("What is the lower bound of your range? (inclusive)\n"))
upperBound = eval(input("What is the upper bound of your range? (inclusive)\n"))
for x in range(lowerBound, upperBound+1):
    if x % 3 == 0:
        print(x)
    elif x % 5 == 0:
        # its important to use elif, otherwise a number like 15 will be printed twice because it is a multiple
        # of 3 and 5
        print(x)
    elif x % 8 == 0:
        print(x)
