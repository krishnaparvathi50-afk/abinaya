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
    
    num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print("Sum of digits:", sum)

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
    
c = float(input("Enter temperature in Celsius: "))

f = (c * 9/5) + 32

print("Temperature in Fahrenheit:", f)


num = int(input("Enter a number: "))

for i in range(1, num+1):
    if num % i == 0:
        print(i)
        
        
num = int(input("Enter a number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")