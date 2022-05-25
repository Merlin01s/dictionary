# Q42.
# Write a Python program to check all values are same in a dictionary. Go to the editor
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False

students={"cierra vega":12,"alden cantrell":12,"kierra gentry":12,"pierre cox":12}
n=int(input("enter :"))
m=list(students.values())
for x in m:
    if x==n:
        print("true")
        break
    else:
        print("false")
        break


