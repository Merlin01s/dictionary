# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}

# a=[1,2,3,4]
# c={}
# n=c
# for i in a:
#     c[i]={}
#     c=c[i]
# print(n)



a=[1,2,3,4]
dict={}
this_dict=dict
for i in a:
    dict[i]={}
    dict=dict[i]
print(this_dict)