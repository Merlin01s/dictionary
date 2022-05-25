# Q30.Write a Python program to remove spaces from dictionary keys.
# Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 

my_dict={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# for key in my_dict:
#     new_key = key.replace(' ', '')
#     my_dict[new_key] = my_dict.pop(key)
# print(my_dict)

dic={}
for i, j in my_dict.items():
    for k in " ":
        i=i.replace(k,'')
        dic[i]=j
print(dic)



