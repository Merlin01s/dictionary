# Q6.
# Write a Python script to add a key to a dictionary.

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

d1={0:10,1:20}
d1.update({2:30})
print(d1)
