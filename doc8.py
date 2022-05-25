# Q8.
# Write a Python program to check whether a given key already exists in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def keypresent(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
keypresent(5)
keypresent(9)

n={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key(i):
    if i in n:
        print("yes ")
    else:
        print("no")
key(5)

a={"v":0,"a":2,"d":4}
def key(i):
    if i in a:
        print("yes")
    else:
        print("no")
key("v")