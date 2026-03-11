s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in s1+s1:
    print("Rotation")
else:
    print("Not Rotation")
    
    
    
    s = input("Enter string: ")

vowels = "aeiou"

result = ""

for ch in s:
    if ch.lower() in vowels:
        result += ch.upper()
    else:
        result += ch

print(result)


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

common = set(s1) & set(s2)

print("Common characters:", common)


words = ["flower","flow","flight"]

prefix = words[0]

for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print("Longest prefix:", prefix)


s = input("Enter string: ")

count = 0

for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub = s[i:j]
        if sub == sub[::-1]:
            count += 1

print("Palindromic substrings:", count)


s = input("Enter string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)



s = input("Enter string: ")

sorted_str = ''.join(sorted(s))

print("Sorted string:", sorted_str)
