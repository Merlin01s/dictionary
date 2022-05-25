# Q35. Write a Python program to count the number of items in a dictionary value that is a list.
# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# Sample output: 5

dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']
}
c=0
for i in (dict1):
    for j in dict1[i]:
        c+=1
print(c)