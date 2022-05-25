# Q13.Write a Python program to sum all the items in a dictionary.

def sum(a):
    s=0
    for i in a.values():
        s+=i
    return s
a={"a":12,"b":13,"c":14}
print("dictionary",a)
print("sum",sum(a))


def sum():
    s=0
    for i in a.keys():
        s+=i
    print(s)
a={1:10,2:20,3:30,4:40}
print("dict",a)
sum()

a={"i":12,"12":3,"b":4}
s=0
for i in a.values():
    s+=i
print(s)