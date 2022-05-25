# Q23.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

my_dict={1:12,2:32,54:12,4:23}
fm=0
sm=0
tm=0
for i in my_dict:
    if my_dict[i]>fm:
        fm=my_dict[i]
for j in my_dict:
    if my_dict[j]>sm and my_dict[j]<fm:
        sm=my_dict[j]
for k in my_dict:
    if my_dict[k]<sm and my_dict[k]>tm:
        tm=my_dict[k]
print(fm,"1st max")
print(sm,"2nd max")
print(tm,"3rd max")