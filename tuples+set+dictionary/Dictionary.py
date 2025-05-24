#empty
d={ }
print(d)
print(type(d))


d1={'name':'shrey','gender':'name'}
print(d1)

d2={(1,2,3):1,'hello':'world'}
print(d2)

#2d dictionary
s={'name':'shrey',
       'clg':'csvtu',
       'sem':'2',
       'subjects':{
           'dsa':95,
           'maths':97,
           'English':94
       }
   }
print(s)
#editing key value pair 
s['subjects']['dsa']=99
print(s)
#using sequence and dict function 
d4 = dict([(1,2),(2,2),(3,3)])
print(d4)


#duplicate keys 

d5={'name':'shrey','name':'nitesh'}
print(d5)

#mutual items as keys
d6={'name':'nitin',(1,2,3):2}      #tupple -->> immutable is the reason it is working    
print(d6)

