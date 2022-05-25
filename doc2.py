# a={str:"w3resource"}
# s="w3resource"
s="i am from navgurukul"
# s=a.split()
b={}
for i in s:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)
    