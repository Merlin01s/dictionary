# Q21.Write a Python program to print all unique values in a dictionary. 

# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

#...................................```
# Syntax : set(iterable)
# Parameters : Any iterable sequence like list, tuple or dictionary.
# Returns : An empty set if no element is passed. Non-repeating element
# iterable modified as passed as argument
# # ..................................````. 
 

a=[{"V":"S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print("Original List: ",L)
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)
s=set()
for i in a:
    for j in i.values():
        s.add(j)
print(s)