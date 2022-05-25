# Q45.# Write a Python program to remove a specified dictionary from a given list. 
# Original list of dictionary:
# [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'},
# {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'},
# {'id': '#808000', 'color': 'Olive'}]

# def remove_dictionary(colors, r_id):
#     colors[:] = [d for d in colors if d.get('id') != r_id]
#     return colors

# colors = [{"id" : "#FF0000", "color" : "Red"}, 
#           {"id" : "#800000", "color" : "Maroon"}, 
#           {"id" : "#FFFF00", "color" : "Yellow"}, 
#           {"id" : "#808000", "color" : "Olive"}] 
# print('Original list of dictionary:')
# print(colors)
# r_id = "#FF0000"
# print("\nRemove id",r_id,"from the said list of dictionary:")
# print(remove_dictionary(colors, r_id))




my_list = [{"id" : 1, "data" : "Python"},
   {"id" : 2, "data" : "Code"},
   {"id" : 3, "data" : "Learn"}]

# print("The list is :")
# print(my_list)

# for index in range(len(my_list)):
#    if my_list[index]['id'] == 2:
#       del my_list[index]
#       break

# print("The result is :")
# print(my_list)


for i in range(len(my_list)):
   if my_list[i]['id']==2:
      del my_list[i]
      break
print(my_list)