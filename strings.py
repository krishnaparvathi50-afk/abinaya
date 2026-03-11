string=("Hello,World!")
print("Reversed string is",string[::-1])

vowels="aeiou"
count=0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels in the string is:", count)

text=input("Enter a string: ")
result=""
for ch in text:
    if ch =="":
        result +=""
    else:
        result +=ch
        print(result)
        
        
text = input("Enter a string: ")

reverse = ""
for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
    
    text = input("Enter a sentence: ")
words = text.split()

max_length = 0

for word in words:
    count = 0
    for ch in word:
        count += 1
    
    if count > max_length:
        max_length = count

print("Longest word length:", max_length)

text = input("Enter a string: ")
result = ""

for ch in text:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch
print(result)

text = input("Enter a string: ")
char = input("Enter character to count: ")

count = 0

for ch in text:
    if ch == char:
        count += 1

print("Count:", count)


string=input("Enter a digits")
sum=0
for char in string:
    if char.isdigit():
        sum+=int(char)
        print("Remove all digits from the given string")

string="krishna"
vowels="aeiou"
for n in string:
    if n in vowels:
        print(n)