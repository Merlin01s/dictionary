# 29.Write a Python program to sort a list alphabetically in a dictionary
dict={"a":2,"c":3,"b":6}
# for li in (dict.values()):
#     li.sorted(dict)
# print(dict)
b = sorted(dict.keys())
print("Sorted keys",b)  
  
c = sorted(dict.items())
print("Sorted Values",c)  
