lowerBound = eval(input("What is the lower bound of your range? (inclusive)\n"))
upperBound = eval(input("What is the upper bound of your range? (inclusive)\n"))
for x in range(lowerBound, upperBound+1):
    if x % 7 == 0:
        if x % 5 != 0:
            print(x)
