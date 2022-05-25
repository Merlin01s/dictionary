# Q16.Write a Python program to map two lists into a dictionary.

# k=[]
# v=[]
# n=int(input("enter the length;"))
# print("write key")
# for i in range(0,n):
#     x=int(input("enter keys: "+ str(i+1)+"="))
#     k.append(x) 
# print("write values")
# for i in range(0,n):
#     x=int(input("enter values: "+ str(i+1)+"="))
#     v.append(x)
# nary=dict(zip(k,v))
# print(nary)   


d=[]
e=[]
w=int(input("enter: "))
print("writekeys")
for i in range(0,w):
    x=int(input("enter keys:"+str(i+1)+"="))
    d.append(x)
print("enter values")
for i in range(0,w):
    x=int(input("enter values"+str(i+1)+"="))
    e.append(x)
a=dict(zip(d,e))
print(a)