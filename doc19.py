# Q19.
# Write a Python program to remove duplicates from Dictionary.
# student_data = {'id1': 
#    {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id2': 
#   {'name': ['David'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id3': 
#     {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id4': 
#    {'name': ['Surya'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
# }

# Sample output:

# {'id2': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['David']}, 'id4': {'subje
# ct_integration': ['english, math, science'], 'class': ['V'], 'name': ['Surya']}, 'id1': {'subject_integration'
# : ['english, math, science'], 'class': ['V'], 'name': ['Sara']}} 

student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

# result = {}

# for key,value in student_data.items():
#     if value not in result.values():
#         result[key] = value

# print(result)


r={}
for k,v in student_data.items():
  if v not in r.values():
    r[k]=v
print(r)