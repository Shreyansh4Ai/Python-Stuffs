#unpacking 
a,b,c=(1,2,3)
print(a,b,c)   #this is unpacking >>note<<---->>LHS = RHS is a necessary but hectic in case of so many elements 

a,b,*others=(1,2,3,4,2,6,56,43,2,9) 
print(b,a,others)
           # others m jo bhi h vo sab ek list bnke ek sath ayega 
           
           
           
           #zipping 
t=(1,2,3)
t1=(9,8,7)
zip(t,t1)
#now to unzip we need a data structure to unzip it so 

print(list(zip(t,t1)))   # saare items list k format m ayenge 
print(tuple(zip(t,t1)))            #sarre items tuple bnke ayenge 
