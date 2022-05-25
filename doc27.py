# Q27.Write a Python program to count the values associated with key in a dictionary.
# student = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# Sample input if key is id: then 6

my_list = [{'id': 1, 'success': True, 'name': 'Lary'},
           {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]
s=0
for i in my_list:
    if 'success' in i:
        if i['success']== True:
            s+=1
print(s)

# success_count = 0
# for dictionary in my_list:
#     if 'success' in dictionary:
#         if dictionary['success'] == True:
#             success_count += 1
# print(success_count) 
