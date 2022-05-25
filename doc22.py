# Q22. Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
        
a={'1':['a','b'],'2':['c','d']}
b=list(a.values())
for i in b[0]:
    for j in b[1]:
        print(i+j)



# my_dict = {'1':['a','b'], '2':['c','d']}

# my_list = list(my_dict.values())
# print(my_list)
# for i in my_list[0]:
#     for j in range(1, len(my_list)):
#         for x in my_list[j]:
#             my_string = i + x
#             print(my_string)
