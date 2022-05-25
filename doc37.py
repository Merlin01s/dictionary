# Q37.Write a Python program to create a dictionary of keys x, y, and z
# where each key has as value a list from 11-20, 21-30, and 31-40 respectively. 
# Access the fifth value of each key from the dictionary.
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]

dict_nums={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
      'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
      'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]
      }

print(dict_nums["x"][4])
print(dict_nums["y"][4])
print(dict_nums["z"][4])
for k,v in dict_nums.items():
   print(k, "has value", v)