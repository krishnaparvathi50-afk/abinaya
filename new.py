string="krishna"
vowels="aeiou"
for n in string:
    if n in vowels:
        print(n)
sentence="i am an intren"
long=0
words=sentence.split()
print(words)
for n in words:
    if len(n)>long:
            long=len(n)
            break
print(long) 