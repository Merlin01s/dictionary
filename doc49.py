# Q49.Python: Access dictionary key’s element by index
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# physics
# math
# chemistry

num = {'physics': 80, 'math': 90, 'chemistry': 86}
a=num.keys()
print(a)
b=list(a)
print(b)
for i in b:
    print(i)