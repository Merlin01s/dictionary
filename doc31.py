# Q31.. Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

Sample_data={"item1":45.50,"item2":35,"item3":41.30,"item4":55,"item5":24}
list1=list(Sample_data.values())
print(list1)
top_one=0
top_two=0
top_three=0
i=0
while i<len(list1):
    if list1[i]>top_one:
        top_one=list1[i]
    i+=1
j=0
while j<len(list1):
    if list1[j]<top_one and list1[j]>top_two:
        top_two=list1[j]
    j+=1
k=0
while k<len(list1):
    if list1[k]>top_three and list1[k]<top_two:
        top_three=list1[k]
    k+=1
print(top_one)
print(top_two)
print(top_three)