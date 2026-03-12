t=(20,40,50,30,10,70)
print(t[::2])

t1=(2,6,5,8,1)
t2=(5,9,8,2,0)
for i in t1:
    if i in t2:
        print(i)
        
        
t=(4,6,8,9,0,5,1)
freq={}
for i in t:
    if i in freq:
        freq[i]+=1
    else:
         freq[i]=1
print(freq)


#concatenate multiple tuples dynamically.
t1=(1,2,3,4,5)
t2=(6,7,8,9,10)
t3=(1,9,4,7,6)
result=t1+t2+t3
print(result)

List = [(1,"apple"),(2,"orange"),(3,"mango")]
result = dict(List)
print(result)


t = (1, 2, 3, 4, 5, 6, 7)

for i in t:
    if i % 2 != 0:
        print(i)
        
t = ('a', 'b', 'c')

s = ''.join(t)
print("String:", s)

t2 = tuple(s)
print("Tuple:", t2)

t = (10, 5, 8, 20, 15)

list = list(t)
list.sort()
print("Second largest:", list[-2])

t = (1, 2, 3, 4, 5)

for i in reversed(t):
    print(i)
    
t = (1, 2, 3, 2, 4, 3, 5)

new_tuple = tuple(set(t))

print(new_tuple)






test