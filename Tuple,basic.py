t=("krishna","abi","muthu","valar","parvathi","selvi",)
print(t[0])
print(t[1])
print(t[2])


t=("apple","orange","banana",)
item="mango"
if item in t:
    print("Element exist in tuple")
else:
    print("Element not found")
    
    
t1=("pink","blue","red",)
t2=("yellow","black","green",)
result=t1+t2
print(result)


t=(1,9,6,5,3)
maximum=max(t)
minimum=min(t)
print("difference",maximum-minimum)

t=[1,2,3,4]
l=list(t)
l.append(5)
print(l)


a=10
b=20
a,b=b,a
print("a=",a)
print("b=",b)

t = (10, 20, 30, 40, 50)
total = sum(t)
print("Sum of elements:", total)


t = (1, 2, 3, 2, 4, 2, 5)
count = t.count(2)
print("Number of times 2 appears:", count)



