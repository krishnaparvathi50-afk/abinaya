num = int(input("Enter a mark: "))

pass_mark = 40

# Using if-else
if num >= pass_mark:
    print("Pass")
else:
    print("Fail")

# Using ternary 
num = int(input("Enter a mark again: "))
print("Pass" if num >= pass_mark else "Fail")

num1=int(input("Enter a first variable: "))
num2=int(input("Enter a second variable: "))
swap=num1 and num2
num1=num2
print("First variable:", num1)
print("Second variable:", num2)
print("swapping two variables:")
num1=num1^num2
num2=num1^num2
print("result of swapping:",num1,num2)

a=int(input("Enter a  first number: "))
b=int(input("Enter a  second number: "))
c=int(input("Enter a third number: "))
if (a < b and a < c):
    print("Smallest number is:", a)
elif (b < a and b < c):
    print("Smallest number is:", b)
else:
    print("Smallest number is:", c)
if (a>b and a>c):
    print("using nested if-else:")
else:
    print("accept 3 numbers and find smallest using nested if-else:")
    
    # Leap year program

leap_year = int(input("Enter a year: "))

if (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
    print(leap_year, "is a leap year")
else:
    print(leap_year, "is not a leap year")


# Day program
logistic = int(input("Enter a number (1-2): "))

if logistic == 1:
    print("Monday")
elif logistic == 2:
    print("Tuesday")
else:
    print("Invalid day")

print("Result:", logistic)


num = int(input("Enter a number: "))

if num % 11 == 0:
    print(num, "is divisible by 11")
else:
    print(num, "is not divisible by 11")
    
    
# Accept angle from user
angle = float(input("Enter the angle in degrees: "))

# Check for types
if angle == 90:
    print("Right Angle")
elif angle < 90 and angle > 0:
    print("Acute Angle")
elif angle > 90 and angle < 180:
    print("Obtuse Angle")
elif angle == 180:
    print("Straight Angle")
else:
    print("Reflex Angle or invalid input")
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

max_num = (a>b and a>c and a) or (b>a and b>c and b) or c

print("Maximum number:", max_num)

ch = input("Enter a character: ")

if ch >= 'A' and ch <= 'Z':
    print("Uppercase letter")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase letter")
else:
    print("Not an alphabet")
    
    import sys

ch = input("Enter a character: ")
print("ASCII value:", ch.encode()[0])

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping using addition and subtraction
a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)