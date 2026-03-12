list=[3,13,25]
for num in list:
    s=0
    for digit in str(num):
        s +=int(digit)
    print("sum of digits of", num,s )
    
        
list=[3,5,8,13,20,22]
odd=[]
even=[]
for num in list:
    if num%2 ==0:
        even.append(num)
    else:
        odd.append(num)
print("even numbers:",even)
print("odd numbers:",odd)


list1=[1,2,3,4,5]
list2=[2,1,6,7,8]
common=[]
for i  in list1:
    if  i in list2:
        common.append(i)
print("common numbers",common)

#Remove duplicates from list without set().
list=[9,7,5,4,3,3,4,9,7]
unique=[]
for i in list:
    if i not in unique:
        unique.append(i)
print(unique)        
 
a=[1,2,3,4]
b=[1,7,6,4]
c=[1,5,8,4]
intersection=[]
for i in a:
    if i in b and c:
        intersection.append(i)
print(intersection)

list=[1,3,5,6,7]
maximum=max(list)
minimum=min(list)
print("difference:",maximum-minimum)

#Find all pairs with given difference k
list=[1,2,3,4,5]
k=3
for i in list:
    for j in list:
        if i-j==k:
            print(i,j) 

#Rotate list left by one element.
list = [1,2,3,4,5]
first = list[0]
for i in range(1,len(list)):
    list[i-1] = list[i]
list[-1] = first
print(list)

list = [1,5,2,3,7,3]
for i in list:
    print(i, ":", list.count(i)) 
    
list = [2,3,4,5,6,7,8,9]
result = []
for num in list:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if not is_prime:
            result.append(num)
print("without primenumber:", result) 
         


print