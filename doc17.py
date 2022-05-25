# # Q17.Write a Python program to sort a dictionary by key.

dict1 = {1: 1, 2: 9, 3: 4}
sorted_values = sorted(dict1.values())
sorted_dict = {}
for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break
print(sorted_dict)


# a={1:12,2:23,5:13,4:42}
# sv=sorted(a.values())
# sd={}
# for i in sv:
#     for j in a.keys():
#         if a[j]==i:
#             sd[j]=a[j]
#             break
# print(sd)

# a={1:12,2:23,5:13,4:42}
# sv=sorted(a.keys())
# sd={}
# for i in sv:
#     for j in a.values():
#         if a[j]==i:
#             sd[j]=a[j]
#             break
# print(sd)