# Q20.Write a Python program to check a dictionary is empty or not.

# dict = {}
# if not dict:
#     print('The dictionary is empty.')
# else:
#     print('The dictionary is not empty.')
    
# def nary(b):
#     if not dict:
#         print("yes it is empty")
#     else:
#         print("no it is not empty")
# nary(b={})
    

# Write a Python program to combine two dictionary adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1={'a': 100, 'b': 200, 'c':300}
# d2={'a': 300, 'b': 200, 'd':400}
# d3={}
# for i,j in d1.items():
#     for x,y in d2.items():
#         if i==x:
#             d3[i]=(j+y)
# print(d3)
# Myresults={'a': 400, 'b': 400}

d1={'a': 100, 'b': 200, 'c':300}
d2={'a': 300, 'b': 200, 'd':400}
d3=dict(d1) # don't do `d3=d1`, I need to make a copy
d3.update(d2) 
for i,j in d1.items():
    for x,y in d2.items():
        if i==x:
            d3[i]=(j+y)
print(d3)
