d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d1:
#     if i in d2:
#         d1[i]=d1[i]+d2[i]
# print(d1)
d3=dict(d1)
d3.update(d2)
# print(d3)
for i, j in d1.items():
    for x, y in d2.items():
        if i==j:
            d3[i]= j+y
print(d3)