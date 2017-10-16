# calculator made with basic methods using Python

print("Welcome to PyCalc")
    # greeting
operator = eval(input("Please enter 1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division"
                 "\nand 5 for exponential multiplications\n"))
num1 = eval(input("First number: "))
num2 = eval(input("Second number: "))

## eval(input) checks to see what type of data is inputted. This is what you use when you want the variable not to be a string


if operator == 1:
    # remember to use == for comparing two different variables
    print(num1+num2)
if operator == 2:
    print(num1-num2)
if operator == 3:
    print(num1*num2)
if operator == 4:
    print(float(num1)/num2)
    # float(int) is called casting. We will go over this in the next session.
if operator == 5:
    print(num1**num2)
    # the ** operator is the power function which means it does: n^n.
