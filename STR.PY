sentence = input("Enter a sentence: ")

words = sentence.split()
freq = {}

for word in words:
    freq[word] = freq.get(word,0) + 1

print(freq)

import string

text = input("Enter a string: ")

for ch in string.punctuation:
    text = text.replace(ch,"")

print("Without punctuation:", text)

s = input("Enter string: ")

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
    
    
    
  