# Q5.
# Write a Python program to sort (ascending and descending) a dictionary by value.

# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

# import operator

# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print('Original dictionary : ',d)
# sorted_d = sorted(d.items(), key=operator.itemgetter(1))
# print('Dictionary in ascending order by value : ',sorted_d)
# sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
# print('Dictionary in descending order by value : ',sorted_d)


dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
b = sorted(dict.keys())
print("Sorted keys",b)  
  
c = sorted(dict.items())
a={}
for i in range(1,16):
    a[i]=i*i
print(a)
print("Sorted Values",c)  

a= {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
b=list(a.keys())
c=list(a.values())
print(b)
print(c)
com=[]
i=0
while i<len(b):
    while i<len(c):
        com.append(b[i])
        com.append(c[i])
        i+=1
print(com)
i=0
while i<len(com):
    j=0
    while j<len(com):
        if com[i]<com[j]:
            a=com[i]
            b=com[j]
            com[i]=b
            com[j]=a
        j+=1
    i+=1
print("ascending",com)