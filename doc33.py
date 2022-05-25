# Q33.Python: Print a dictionary line by line
# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# Sample Output:

# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2        
# Puja                                                                                                          
# class : V                                                                                                     
# roll_id : 3 


students={"Aex":{"class":"V",
                 "rolld_id":2},
          "puja":{"class":"V",
                  "rolld_id":3}}
for x in students:
    print(x)
    for y in students:
        print(x,":",students[y])
        