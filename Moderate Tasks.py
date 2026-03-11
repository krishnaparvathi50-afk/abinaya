s = input("Enter a string: ")

digits = 0
letters = 0
special = 0

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special characters:", special)

num = int(input("Enter a number: "))

print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hexadecimal:", hex(num))

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)
    
    num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit**3
    temp = temp // 10

if num == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
    
    
    
    c = float(input("Enter temperature in Celsius: "))

f = (c * 9/5) + 32

print("Temperature in Fahrenheit:", f)