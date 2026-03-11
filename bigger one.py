a = 3
b = 13

if a > b:
    print(a, "is bigger than", b)
else:
    print(b, "is bigger than", a)

print("compare two numbers and find the bigger number")

word=input("Enter a word: ")
if word[0] in 'aeiouAEIOU':
    print("word contains the letter 'a'")
    
a = int(input("Enter a number: "))

if a > 0:
    print("This is a positive number")
elif a < 0:
    print("This is a negative number")
else:
    print("This is zero")

print("Check if a number is positive, negative or zero")

a = int(input("Enter a number: "))

if a % 2 == 0:
    print(a, "is an even number")
else:
    print(a, "is an odd number")
    
    print("check if a number is even or odd")
    
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    remainder =a%b
    print("Remainder is",remainder)
    
    num=int(input("Enter a number: "))
    if 10<=num<=50:
        print(num,"is between 10 and 50")
    else:
        print(num,"is not between 10 and 50")
        
        
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = x * y
print("Multiplication result:", result)

if result > 100:
    print("Result is greater than 100")
else:
    print("Result is NOT greater than 100")