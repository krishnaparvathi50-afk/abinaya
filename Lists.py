"""#Create a list of fruits and print the second and last fruit

fruits = ["Apple", "Orange", "Pineapple", "Grapes"]


print(fruits[1])
print(fruits[-1])
"""
"""
#Add mango to the list remove apple

fruits = ["Apple", "Orange", "Pineapple", "Grapes"]

fruits.append("Mango")

print(fruits)

if "App" in fruits:
    fruits.remove("Apple")
else:
    print("There is no App")
    
print(fruits)

"""
"""
# sort a list of numbers in decending order

listed_numbers = [2,5,7,8,6,17,12,0,9,11]
print(listed_numbers)

listed_numbers.sort(reverse=True)

print(listed_numbers)

print(listed_numbers[::-1])"""

"""
#Create a 10 Numbers and print only the even numbers

numbers = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(numbers)):
    if i % 2 != 0:
        print(i)
"""

# Take a list of names and check if a given name (user input) is present in the list or not
"""
names = ["karthick", "Rahul", "Baisal", "Suresh", "Selva"]

name = input("Enter the name: ")

if name.lower() in names:
    print(f"Yes {name} is present")
else:
    print(f"Not exist")
"""

# write a program to reverse the list without the inbuilt reverse funtion

# Create a nested list and print the second element of the inner list


dual = [[1,2,3,4,5], [6,7,8,9,10]]

print(dual[1][1])

